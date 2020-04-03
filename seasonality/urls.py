from django.urls import path

from . import views

app_name = 'seaonality'
urlpatterns = [
    path('add_seasonality/', views.add_seasonality, name='add_seasonality'),
    path('view_seasonality/', views.view_seasonality_value, name='view_seasonality'),
    path('edit_seasonality/', views.edit_seasonality, name='edit_seasonality'),
    path('update_seasonality/', views.update_seasonality, name='update_seasonality'),
    path('add_seasonality_value/', views.add_seasonality_value, name='add_seasonality_value'),
    path('edit_seasonality_value/', views.edit_seasonality_value, name='edit_seasonality_value'),
    path('update_seasonality_value/', views.update_seasonality_value, name='update_seasonality_value'),

]