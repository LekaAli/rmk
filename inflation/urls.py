from django.urls import path
from . import views

app_name = 'inflation'
urlpatterns = [
    path('InflationInput/' , views.InflationInput.as_view(), name= 'InflationInput'),

]