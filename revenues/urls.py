from django.urls import path
from . import views

app_name = 'revenues'
urlpatterns = [
    path('RevenueInput' , views.RevenueInput.as_view(), name= 'RevenueInput'),  

]