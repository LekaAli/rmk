from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.template import Context, TemplateDoesNotExist


def html_to_pdf_creator(app_name='revenues', html_template='report.html'):
	try:
		# Load and return a template for the given name
		template_name = '/'.join([app_name, html_template])
		print('STRING: ', template_name, type(template_name))
		template = get_template(template_name)
		context = Context({'pagesize': 'A4'})
		html = template.render({'pagesize': 'A4'})
		results = BytesIO()
		pdf = pisa.pisaDocument(html, dest=results)
	except Exception as ex: # TemplateDoesNotExist:
		return HttpResponse(ex)
	return HttpResponse(results.getvalue(), content_type='application/pdf')
