# from revenues.models import Revenue
#
#
# def apply_default(func):
# 	def wrapper_function(*args, **kwargs):
# 		revenue_years = set(Revenue.objects.values_list('financial_year', flat=True))
# 		if len(revenue_years) in [1]:
# 			return func(*args, **kwargs)
# 		return
# 	return wrapper_function
