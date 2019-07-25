from django.urls import path
from . import views

app_name = 'dates'
urlpatterns = [
    path('CreateDates/' , views.CreateDates.as_view(), name= 'CreateDates'), 
    ]