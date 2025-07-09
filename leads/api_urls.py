from django.urls import path
from .api_views import LeadListCreateAPIView

urlpatterns = [
    path('leads/', LeadListCreateAPIView.as_view(), name='api_leads'),
]
