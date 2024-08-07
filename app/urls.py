from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jogadoras/', views.jogadoras, name='jogadoras'),
    path('sobre/', views.sobre, name='sobre'),
]
