# from seasonality.models import ProductSeasonality
#
#
# def product_seasonality_months(months):
#     allocated_seasons_month = ProductSeasonality.objects.values_list('month', flat=True)
#     return [obj for obj in months if obj[0] not in allocated_seasons_month]
