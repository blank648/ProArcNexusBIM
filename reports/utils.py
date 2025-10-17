import io
import base64
from django.db.models import Sum
import matplotlib.pyplot as plt
from django.template.loader import render_to_string
from weasyprint import HTML
from estimates.models import Deviz

#agrega Sum('valoare_totala') din Deviz grupate dupa client__denumire.
def get_valoare_totala_per_client(start_date, end_date, client=None):
    qs = Deviz.objects.select_related('client').filter(
        data_emitere_range = (start_date, end_date)
    )
    if client:
        qs = qs.filter(client=client)

    results = qs.values('client_denumire').annotate(suma=Sum('valoare_totala'))
    data = [{'denumire': r['client__denumire'], 'suma': r['suma'] or 0} for r in results]
    return data

def get_total_pe_perioada(start_date, end_date, client=None):
    qs = Deviz.objects.filter(data_emitere_range=(start_date, end_date))
    if client:
        qs = qs.filter(client=client)
    total = qs.aggregate(total=Sum('valoare_totala'))['total'] or 0
    return total

def generate_bar_chart(data):
    labels = [d['denumire'] for d in data]
    values = [d['suma'] for d in data]
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xlabel('Client')
    ax.set_ylabel('Valoare totala')
    ax.set_title('Valoare totala per client')
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('ascii')
    return f"data:image/png;base64,{img_base64}"

def export_report_pdf(context):
    html_string = render_to_string('reports/reports_pdf.html')
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    from django.http import HttpResponse
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f"attachment; filename=report_{context.get('start_date')}_{context.get('end_date')}.pdf"
    return response

