
import aspose.pdf as ap

input_pdf = "little_html.html"
output_pdf = "convert_html_to_pdf.pdf"
options = ap.HtmlLoadOptions()
document = ap.Document(input_pdf, options)
document.save(output_pdf)

from django.shortcuts import render,redirect,HttpResponse


def render_pdf_view(request):
    template_path = "home\preview_offerletter.html"
    context = {}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
