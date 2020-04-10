from django.urls import path
from . import views

app_name = 'dates'
urlpatterns = [
    path('AddDates/', views.create_dates, name='AddDates'),
    path('CreateDates/', views.advanced_create_dates, name='CreateDates'),
    path('ViewDates/', views.view_dates, name='ViewDates'),
    path('ViewInflation/', views.view_inflation, name='ViewInflation'),
    path('EditDates/', views.edit_dates, name='EditDates'),
    path('UpdateDates/', views.update_dates, name='UpdateDates'),
    path('ManageInflation/', views.manage_inflation_values, name='ManageInflation'),
    path('EditInflation/', views.edit_inflation, name='EditInflation'),
    path('UpdateInflation/', views.update_inflation, name='UpdateInflation'),
    ]
