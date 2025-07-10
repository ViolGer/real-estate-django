from django.urls import path, include
from . import views
from listings.api import PropertyDetailAPI, ToggleFavoriteAPI

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_property, name='add_property'),
    path('property/<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('property/<int:pk>/delete/', views.delete_property, name='delete_property'),
    #path('profile/', views.profile_view, name='profile'),
    path('', include('users.urls')),
    path('api/', include('leads.api_urls')),
    path('quizzes/', include('quizzes.urls')),
    path('api/', include('listings.api_urls')),
    path('api/property/<int:pk>/', PropertyDetailAPI.as_view(), name='PropertyDetailAPI'),
    path('api/property/<int:pk>/favorite/', ToggleFavoriteAPI.as_view(), name='toggle_favorite_api'),
    ]