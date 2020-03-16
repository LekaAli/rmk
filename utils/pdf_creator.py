from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.template import Context, TemplateDoesNotExist
from importlib import import_module


class EngineSelector(object):
	def __init__(self, app_name):
		self.app_engine = import_module('%s' % app_name)


def html_to_pdf_creator(app_name='revenues', html_template='report.html'):
	try:
		# Load and return a template for the given name
		template_name = '/'.join([app_name, html_template])
		template = get_template(template_name)
		# engine and data selection
		engine = EngineSelector(app_name)
		data = {}
		if engine.app_engine.AppEngine:
			data = engine.app_engine.AppEngine.generate_report_data()
		html = template.render({
			'view_option': '',
			'title': 'Revenue Predictions',
			'report_data': data
		})
		results = BytesIO()
		pdf = pisa.pisaDocument(html, dest=results)
	except Exception as ex:  # TemplateDoesNotExist:
		return HttpResponse(ex)
	return HttpResponse(results.getvalue(), content_type='application/pdf')
