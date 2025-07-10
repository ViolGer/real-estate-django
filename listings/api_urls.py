from django.urls import path
from .api import PropertyDetailAPI

urlpatterns = [
    path('property/<int:pk>/', PropertyDetailAPI.as_view(), name='property_detail_api'),
]
