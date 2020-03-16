from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'businessplan'
urlpatterns = [
    path('BusinessInfo/', views.BusinessInfo.as_view(), name= 'BusinessDetails'),
    path('PromoterCreator/', views.PromoterCreator.as_view(), name= 'PromoterCreator'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    
]