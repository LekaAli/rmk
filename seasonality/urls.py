from django.urls import path
from . import views

app_name = 'seaonality'
urlpatterns = [
    path('SeasonalityInput/' , views.SeasonalityInput.as_view(), name= 'SeasonalityInput'),

]