from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ,name='covid'),
    path('allcountry/',views.allcountry,name='allcountry')
]