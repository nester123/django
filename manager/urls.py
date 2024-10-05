from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('order/', views.order, name="order"),
    path('login/', views.user_login, name="login"),
     path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
]
