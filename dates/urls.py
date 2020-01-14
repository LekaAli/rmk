from django.urls import path
from . import views

app_name = 'dates'
urlpatterns = [
    path('CreateDates/', views.create_dates, name='CreateDates'),
    path('EditDates/', views.edit_dates, name='EditDates'),
    ]
