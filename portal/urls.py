from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_list, name='app_list'),
    path('<int:pk>/', views.app_detail, name='app_detail'),
    path('add/', views.app_add, name='app_add'),

    
]
