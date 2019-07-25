from django.urls import path
from . import views

app_name = 'rampup'
urlpatterns = [
    path('rampup' , views.RampUpInput.as_view(), name= 'RampUpInput'),  

]