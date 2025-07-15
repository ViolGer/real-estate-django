from django.urls import path
from . import views
urlpatterns = [
    path('', views.collection_list, name='collection_list'),
    path('<int:pk>/', views.collection_detail, name='collection_detail'),
    path('collections/add/<int:property_id>/', views.add_to_collection, name='add_to_collection'),
    path('collections/create/', views.create_collection, name='create_collection'),
]
