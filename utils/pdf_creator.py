from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.template import Context, TemplateDoesNotExist
from importlib import import_module


class EngineSelector(object):
	def __init__(self, app_name):
		self.app_engine = import_module('%s' % app_name)


class YearlyTotal(object):
	def __init__(self, data):
		self.data = data
		self.year_totals = dict()
	
	def tax_year_totals(self):
		self.year_totals['tax'] = {}
		for year, month_tot_dict in self.data.get('tax').items():
			self.year_totals['tax'].update({year: sum(month_tot_dict.values())})
	
	def net_profit_year_total(self):
		self.year_totals['net_profit'] = {}
		for year, month_tot_dict in self.data.get('net_profit').items():
			self.year_totals['net_profit'].update({year: sum(month_tot_dict.values())})
	
	def gross_profit_year_total(self):
		self.year_totals['gross_profit'] = {}
		for year, month_tot_dict in self.data.get('gross_profit_total').items():
			self.year_totals['gross_profit'].update({year: sum(month_tot_dict.values())})
	
	def cost_of_sale_year_total(self):
		self.year_totals['cost_of_sale'] = {}
		for year, month_product_tot_dict in self.data.get('cost_of_sale').items():
			self.year_totals['cost_of_sale'][year] = {}
			for month, product_tot_dict in month_product_tot_dict.items():
				for product, total in product_tot_dict.items():
					if product in self.year_totals['cost_of_sale'][year].keys():
						self.year_totals['cost_of_sale'][year][product] += total
					else:
						self.year_totals['cost_of_sale'][year][product] = total
		for year, product_tot_dict in self.year_totals.get('cost_of_sale').items():
			tot = sum(product_tot_dict.values())
			product_tot_dict.update({'total': tot})

	def profit_before_tax_year_total(self):
		self.year_totals['profit_before_tax'] = {}
		for year, month_tot_dict in self.data.get('profit_before_tax').items():
			self.year_totals['profit_before_tax'].update({year: sum(month_tot_dict.values())})
	
	def expense_year_total(self):
		self.year_totals['expense'] = {}
		for year, expense_kind_tot_dict in self.data.get('yearly_expense_total').items():
			self.year_totals['expense'][year] = {}
			for e_kind, expense_tot_dict in expense_kind_tot_dict.items():
				self.year_totals['expense'][year][e_kind] = {}
				for e_name, e_tot in expense_tot_dict.items():
					if e_name != 'total':
						self.year_totals['expense'][year][e_kind][e_name] = e_tot
		for year, kind_expense_tot_dict in self.year_totals.get('expense').items():
			for kind, expense_tot_dict in kind_expense_tot_dict.items():
				tot = sum(expense_tot_dict.values())
				expense_tot_dict.update({'total': tot})
	
	def revenue_year_total(self):
		self.year_totals['revenue'] = self.data.get('yearly_revenues')
		for year, values_dict in self.year_totals['revenue'].items():
			self.year_totals['revenue'][year].update({'total': sum(values_dict.values())})
	
	def generate_yearly_data(self):
		self.tax_year_totals()
		self.net_profit_year_total()
		self.gross_profit_year_total()
		self.cost_of_sale_year_total()
		self.profit_before_tax_year_total()
		self.expense_year_total()
		self.revenue_year_total()
		self.generate_monthly_revenue()
		
	def generate_monthly_revenue(self):
		self.year_totals['monthly_revenues'] = {}
		for year, product_month_tot_dict in self.data.get('monthly_revenues').items():
			self.year_totals['monthly_revenues'][year] = {}
			for product, month_tot_dict in product_month_tot_dict.items():
				self.year_totals['monthly_revenues'][year][product] = {}
				for tot_lst in month_tot_dict:
					month = tot_lst[3]
					val = tot_lst[4]
					self.year_totals['monthly_revenues'][year][product].update({month: val})
				d = {}
				months = list(self.year_totals['monthly_revenues'][year][product].keys())
				dd = self.year_totals['monthly_revenues'][year][product]
				months.sort()
				for month in months:
					d[month] = dd.get(month)
				self.year_totals['monthly_revenues'][year][product] = d
		

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
			year_total = YearlyTotal(data)
			year_total.generate_yearly_data()
			data.update({
				'all_yearly_totals': year_total.year_totals
			})
			data['monthly_revenues'] = year_total.year_totals.get('monthly_revenues')
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
