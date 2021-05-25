from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="weatherhome"),
    path('weather/', views.weather, name='weather'),
]