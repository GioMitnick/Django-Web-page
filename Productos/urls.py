
# Productos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Productos, name='Productos'),
    path('info/<int:id>/', views.info_productos, name='info_productos'),
]
