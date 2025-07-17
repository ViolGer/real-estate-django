from django.urls import path
from . import views
urlpatterns = [
    path('', views.collection_list, name='collection_list'),
    path('<int:pk>/', views.collection_detail, name='collection_detail'),
    path('collections/add/<int:property_id>/', views.add_to_collection, name='add_to_collection'),
    path('create/', views.create_collection, name='create_collection'),
    path('<int:pk>/', views.edit_collection, name='edit_collection'),
    path('remove/<int:collection_id>/<int:property_id>/', views.remove_from_collection, name='remove_from_collection'),

]
