from django.urls import path
from. import views

urlpatterns=[ path ('', views.principal),
             path('Productos',views.Productos),
             path('info/<int:id>', views.info_productos)]