from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.lead_create, name='lead_create'),
    path('my/', views.my_leads, name='my_leads'),
]
