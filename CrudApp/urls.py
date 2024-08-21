from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.RegisterNewUser, name='add'),
    path('', views.ViewUser, name='display_user'),
    path('edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('delete/<int:pk>/', views.delete_user, name='delete_user'),
]
