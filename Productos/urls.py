from django.urls import path
from. import views

urlpatterns=[ path ('', views.principal),
             path('Productos/',views.Productos),
             path('info/', views.info_productos)]