from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [    
    path('', views.index, name="index"),  
    # path('', views.about, name="index"),  

]