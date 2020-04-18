from django.urls import path
from . import views

app_name = 'revenues'
urlpatterns = [
    path('RevenueInput', views.generate_revenue_projection, name='RevenueInput'),
    path('view_revenue', views.view_revenue_projection, name='view_revenue'),

]