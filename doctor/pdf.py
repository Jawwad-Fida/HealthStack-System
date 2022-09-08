from io import BytesIO
from urllib import response
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from .models import Report
from django.template import Context 


def render_to_pdf(template_src, context_dict=()):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),context_type="aplication/pdf")
    return None




def report_pdf(request, pk):
    report=Report.obects.get(report_id=pk)
    context={'report':report,
    }
    pdf=render_to_pdf('report_pdf.html', report)
    if pdf:
        response=HttpResponse(pdf, context_type='application/pdf')
        content="inline; filename=report.pdf"
        response['Content-Disposition']= content
        return response
    return HttpResponse("Not Found")