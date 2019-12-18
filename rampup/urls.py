from django.urls import path
from . import views

app_name = 'rampup'
urlpatterns = [
    path('add_rampup', views.add_rampup, name='add_rampup'),
    path('add_rampup_value', views.add_rampup_value, name='add_rampup_value'),

]