from django.urls import path

from . import views

app_name = 'seaonality'
urlpatterns = [
    path('add_seasonality/', views.add_seasonality, name='add_seasonality'),
    path('add_seasonality_value/', views.add_seasonality_value, name='add_seasonality_value'),

]