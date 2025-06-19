from django.urls import path

from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_property, name='add_property'),
    path('property/<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('property/<int:pk>/delete/', views.delete_property, name='delete_property'),
    ]