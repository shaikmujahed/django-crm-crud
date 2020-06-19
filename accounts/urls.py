from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.userPage, name='user'),
    path('account/', views.settingsPage, name='account'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<int:pk>', views.update_order, name='update_order'),
    path('delete_order/<int:pk>', views.delete_order, name='delete_order'),
    path('login', views.loginView, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutView, name='logout'),

    # Reset password
    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]