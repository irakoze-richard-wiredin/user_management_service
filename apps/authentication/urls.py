from django.urls import path
from . import views

urlpatterns = [
    path('login', views.custom_login, name='user_login'),
    path('register', views.register, name='user_registration'),
    path('reset-password', views.password_reset, name='user_reset_password'),
    path('reset-password/confirm/<str:uidb64>/<str:token>/', views.password_reset_confirm, name='password_reset_confirm'),
]
