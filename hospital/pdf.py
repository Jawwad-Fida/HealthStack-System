from io import BytesIO
from urllib import response
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from doctor.models import Prescription
from doctor.models import  Prescription,Perscription_medicine,Perscription_test
from hospital.models import Patient
from datetime import datetime


def render_to_pdf(template_src, context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="aplication/pdf")
    return None




def prescription_pdf(request,pk):
 if request.user.is_patient:
    patient = Patient.objects.get(user=request.user)
    prescription = Prescription.objects.get(prescription_id=pk)
    perscription_medicine = Perscription_medicine.objects.filter(prescription=prescription)
    perscription_test = Perscription_test.objects.filter(prescription=prescription)
    current_date = datetime.date.today()
    context={'patient':patient,'current_date' : current_date,'prescription':prescription,'perscription_test':perscription_test,'perscription_medicine':perscription_medicine}
    pdf=render_to_pdf('prescription_pdf.html', context)
    if pdf:
        response=HttpResponse(pdf, content_type='application/pdf')
        content="inline; filename=report.pdf"
        # response['Content-Disposition']= content
        return response
    return HttpResponse("Not Found")
