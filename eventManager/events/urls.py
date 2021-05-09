from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [    
    path('', views.index, name="index"),
    # path('/admin', admin.site.urls, name='admin'),
  
 
]