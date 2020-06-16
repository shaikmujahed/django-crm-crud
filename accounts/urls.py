from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('user/', views.userPage, name='user'),
  path('products/', views.products, name='products'),
  path('customer/<int:pk>/', views.customer, name='customer'),
  path('create_order/', views.create_order, name='create_order'),
  path('update_order/<int:pk>', views.update_order, name='update_order'),
  path('delete_order/<int:pk>', views.delete_order, name='delete_order'),
  path('login', views.loginView, name='login'),
  path('register', views.register, name='register'),
  path('logout', views.logoutView, name='logout')
]