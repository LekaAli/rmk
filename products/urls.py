from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('products/', views.create_product, name='create_product'),
    path('expenses/', views.add_expense, name='add_expense'),
    path('cost_of_sale/', views.create_cost_of_sale, name='add_cost_of_sale'),
    path('products/assignment/', views.create_cost_of_sale, name='product_assignment'),
    path('products/tax_management/', views.create_cost_of_sale, name='tax_management'),

]