from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, UserLoginView, UserLogoutView, ProfileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
]