from django.urls import path
from . import views

app_name = 'rampup'
urlpatterns = [
    path('add_rampup', views.add_rampup, name='add_rampup'),
    path('view_rampups', views.view_rampup_value, name='view_rampups'),
    path('edit_rampup', views.edit_rampup, name='edit_rampup'),
    path('update_rampup', views.update_rampup, name='update_rampup'),
    path('add_rampup_value', views.add_rampup_value, name='add_rampup_value'),
    path('edit_rampup_value', views.edit_rampup_value, name='edit_rampup_value'),
    path('update_rampup_value', views.update_rampup_value, name='update_rampup_value'),

]