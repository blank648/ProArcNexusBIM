from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, View, CreateView
from django.template.loader import render_to_string
from django.http import HttpResponse
from accounts.mixins import RoleRequiredMixin

from weasyprint import HTML

from .models import Deviz
from .forms import DevizForm, LinieDevizFormSet

class DevizListView(RoleRequiredMixin, ListView):
    allowed_roles = ['admin', 'manager', 'user']
    model = Deviz
    template_name = 'estimates/deviz_list.html'
    context_object_name = 'deviz_list'
    paginate_by = 20

    def get_queryset(self):
        q = self.request.GET.get('q','')
        qs = super().get_queryset().select_related('client')
        if q:
            qs = qs.filter(
                Q(numar_deviz__icontains=q) |
                Q(client__denumire__icontains=q) |
                Q(data_emitere__icontains=q)
            )
        return qs

class DevizCreateView(View):
    template_name = 'estimates/deviz_form.html'
    #initiez DevizForm si LinieDevizFormSet
    def get(self, request):
        form = DevizForm()
        formset = LinieDevizFormSet()
        return render(request, self.template_name, {'form': form, 'formset': formset})

    def post(self, request):
        form = DevizForm(request.POST)
        formset = LinieDevizFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            deviz = form.save(commit=False)
            deviz.valoare_totala = 0
            deviz.save()
            total = 0
            for subform in formset:
                if subform.cleaned_data and not subform.cleaned_data.get('DELETE'):
                    linie = subform.save(commit=False)
                    linie.deviz = deviz
                    if not linie.pret_unitar:
                        linie.pret_unitar = linie.articol.pret_standard
                    linie.save()
                    total += linie.cantitate * linie.pret_unitar
            deviz.valoare_totala = total
            deviz.save()
            return redirect('estimates:list')
        return render(request, self.template_name, {'form': form, 'formset': formset})

class DevizUpdateView(View):
    template_name = 'estimates/deviz_form.html'

    def get(self, request, pk):
        deviz = get_object_or_404(Deviz, pk=pk)
        form = DevizForm(instance=deviz)
        formset = LinieDevizFormSet(instance=deviz)
        return render(request, self.template_name, {'form': form, 'formset': formset, 'object': deviz})

    def post(self, request, pk):
        deviz = get_object_or_404(Deviz, pk=pk)
        form = DevizForm(request.POST, instance=deviz)
        formset = LinieDevizFormSet(request.POST, instance=deviz)
        if form.is_valid() and formset.is_valid():
            deviz = form.save(commit=False)
            total = 0
            for subform in formset:
                if subform.cleaned_data:
                    if subform.cleaned_data.get('DELETE'):
                        if subform.instance.pk:
                            subform.instance.delete()
                    else:
                        linie = subform.save(commit=False)
                        linie.deviz = deviz
                        if not linie.pret_unitar:
                            linie.pret_unitar = linie.articol.pret_standard
                        linie.save()
                        total += linie.cantitate * linie.pret_unitar
            deviz.valoare_totala = total
            deviz.save()
            return redirect('estimates:list')
        return render(request, self.template_name, {'form': form, 'formset': formset, 'object': deviz})

class DevizDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = ['admin', 'manager']
    model = Deviz
    template_name = 'estimates/deviz_confirm_delete.html'
    success_url = reverse_lazy('estimates:list')

class DevizPDFView(RoleRequiredMixin, View):
    allowed_roles = ['admin', 'manager', 'user']
    def get(self, request, pk):
        deviz = get_object_or_404(Deviz, pk=pk)
        html_string = render_to_string('estimates/deviz_pdf.html', {'deviz': deviz})
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        pdf = html.write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="deviz_{deviz.numar_deviz}.pdf"'
        return response