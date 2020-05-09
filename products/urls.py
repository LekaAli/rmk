from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('add_n_product/', views.add_n_product, name='add_n_product'),
    path('view_product/', views.view_product, name='view_product'),
    path('products/', views.create_product, name='create_product'),
    path('edit_product/', views.edit_product, name='edit_product'),
    path('update_product/', views.update_product, name='update_product'),
    path('expenses/', views.add_n_expense, name='add_expense'),
    path('add_n_expenses/', views.add_expense, name='add_n_expenses'),
    path('edit_expense/', views.edit_expense, name='edit_expense'),
    path('view_expense/', views.view_expense, name='view_expense'),
    path('update_expense/', views.update_expense, name='update_expense'),
    path('create_cost_of_sale/', views.create_cost_of_sale, name='create_cost_of_sale'),
    path('edit_cost_of_sale/', views.edit_cost_of_sale, name='edit_cost_of_sale'),
    path('view_cost_of_sale/', views.view_cost_of_sale, name='view_cost_of_sale'),
    path('products/add_tax_management/', views.add_tax_value, name='add_tax_management'),
    path('products/edit_tax_management/', views.edit_tax_value, name='edit_tax_management'),
    path('products/update_tax_management/', views.update_tax_value, name='update_tax_management'),
    path('products/view_tax/', views.view_tax_value, name='view_tax'),
    path('products/add_n_taxes/', views.add_n_tax_values, name='add_n_taxes'),

]