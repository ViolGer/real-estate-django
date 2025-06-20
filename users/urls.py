from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]
