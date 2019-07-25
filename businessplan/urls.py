from django.urls import path
from . import views

app_name = 'businessplan'
urlpatterns = [
    path('BusinessInfo/' , views.BusinessInfo.as_view(), name= 'BusinessDetails'),  
    path('PromoterCreator/' , views.PromoterCreator.as_view(), name= 'PromoterCreator'),

    
]