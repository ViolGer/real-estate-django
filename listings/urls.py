from django.urls import path, include
from property_collections import views as collection_views
from listings.api import PropertyDetailAPI, ToggleFavoriteAPI
from . import views

urlpatterns = [
    # UI views
    path('', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_property, name='add_property'),
    path('property/<int:pk>/edit/', views.edit_property, name='edit_property'),
    path('property/<int:pk>/delete/', views.delete_property, name='delete_property'),

    # Collections
    path('collections/', collection_views.collection_list, name='collection_list'),
    path('collections/add/<int:property_id>/', collection_views.add_to_collection, name='add_to_collection'),
    path('collections/remove/<int:collection_id>/<int:property_id>/', collection_views.remove_from_collection, name='remove_from_collection'),
    path('collections/create/', collection_views.create_collection, name='create_collection'),

    # API
    path('api/', include('listings.api_urls')),
    path('api/property/<int:pk>/', PropertyDetailAPI.as_view(), name='PropertyDetailAPI'),
    path('api/property/<int:pk>/favorite/', ToggleFavoriteAPI.as_view(), name='toggle_favorite_api'),

    # Other includes
    path('users/', include('users.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('api/', include('leads.api_urls')),
]
