from django.urls import path
from . import views

urlpatterns = [
    path('<str:slug>/', views.sistemas, name='sistemas'),
    path('export/<str:slug>/', views.export, name='export')
]