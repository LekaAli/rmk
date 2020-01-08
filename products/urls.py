from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('products/', views.create_product, name='create_product'),
    path('expenses/', views.add_expense, name='add_expense'),
    path('cost_of_sale/', views.create_cost_of_sale, name='add_cost_of_sale'),
    path('products/assignment/', views.product_seasonality_rampup_assignment, name='product_assignment'),
    path('products/tax_management/', views.add_tax_value, name='tax_management'),

]