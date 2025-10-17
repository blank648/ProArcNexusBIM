from django.shortcuts import render, redirect
from django.views import View
from .forms import ReportFilterForm
from .utils import(
    get_valoare_totala_per_client,
    get_total_pe_perioada,
    generate_bar_chart,
    export_report_pdf
)
from accounts.mixins import RoleRequiredMixin

class ReportSummaryView(RoleRequiredMixin, View):
    allowed_roles = ['admin', 'manager']
    template_name = 'reports/report_summary.html'
    def get(self, request):
        form = ReportFilterForm(request.GET or None)
        context = {'form': form}
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            client = form.cleaned_data['client']
            per_client = get_valoare_totala_per_client(start, end, client)
            total_all = get_total_pe_perioada(start, end, client)
            chart_url = generate_bar_chart(per_client)
            context.update({
                'per_client': per_client,
                'total_all': total_all,
                'chart_url': chart_url,
            })
        return render(request, self.template_name, context)

class ReportPDFView(RoleRequiredMixin, View):
    allowed_roles = ['admin', 'manager']
    def get(self, request):
        form = ReportFilterForm(request.GET or None)
        if form.is_valid():
            return redirect('reports:summary')
        start = form.cleaned_data['start_date']
        end = form.cleaned_data['end_date']
        client = form.cleaned_data['client']
        per_client = get_valoare_totala_per_client(start, end, client)
        total_all = get_total_pe_perioada(start, end, client)
        context = {
            'per_client': per_client,
            'total_all': total_all,
            'start_date': start,
            'end_date': end,
        }
        return export_report_pdf(context)
