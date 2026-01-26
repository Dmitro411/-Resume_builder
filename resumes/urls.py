from django.contrib import admin
from django.urls import path, include
from .views import resume_detail_view

urlpatterns = [
    path('my/', resume_detail_view, name='resume'),
]