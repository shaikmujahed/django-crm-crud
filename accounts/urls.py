from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('products/', views.products, name='products'),
  path('customer/<str:id>/', views.customer, name='customer'),
  path('create_order/', views.create_order, name='create_order'),
  path('update_order/<int:pk>', views.update_order, name='update_order'),
  path('delete_order/<int:pk>', views.delete_order, name='delete_order'),
]