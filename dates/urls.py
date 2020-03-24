from django.urls import path
from . import views

app_name = 'dates'
urlpatterns = [
    path('AddDates/', views.create_dates, name='AddDates'),
    path('CreateDates/', views.advanced_create_dates, name='CreateDates'),
    path('EditDates/', views.edit_dates, name='EditDates'),
    path('UpdateDates/', views.update_dates, name='UpdateDates'),
    ]
