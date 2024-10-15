from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_login, name='to_login'),
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path('plataforma/', views.plataforma, name='plataforma'),
]