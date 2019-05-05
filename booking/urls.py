from django.urls import path
from . import views 

urlpatterns = [
    path('service', views.service , name='s'),
    path('doctor', views.doctor , name='d'),
    path('book', views.book , name='b'),
    path('contact', views.contact , name='c'),
]