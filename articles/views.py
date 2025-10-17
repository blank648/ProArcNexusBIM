from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Articol
from .forms import ArticolForm
from accounts.mixins import RoleRequiredMixin

class ArticolListView(RoleRequiredMixin, ListView):
    allowed_roles = ['admin','manager','user']
    model = Articol
    template_name = 'articles/articol_list.html'
    paginate_by = 20

    def get_queryset(self):
        q = self.request.GET.get('q','')
        qs = super().get_queryset()
        if q:
            qs = qs.filter(
                Q(cod__icontains=q) |
                Q(denumire__icontains=q)
            )
        return qs

class ArticolCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ['admin','manager']
    model = Articol
    form_class = ArticolForm
    template_name = 'articles/articol_form.html'
    success_url = reverse_lazy('articles::list')

class ArticolUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = ['admin','manager']
    model = Articol
    form_class = ArticolForm
    template_name = 'articles/articol_form.html'
    success_url = reverse_lazy('articles::list')

class ArticolDeleteView(DeleteView):
    allowed_roles = ['admin']
    model = Articol
    template_name = 'articles/articol_confirm_delete.html'
    success_url = reverse_lazy('articles::list')
