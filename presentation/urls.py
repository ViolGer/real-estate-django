from listings.urls import urlpatterns

from django.urls import path
from presentation import views

app_name = "presentation"

urlpatterns = [
    path('<int:pk>/', views.presentation_view, name='presentation_view'),
]