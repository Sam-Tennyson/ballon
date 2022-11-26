from django.contrib import admin
from django.urls import path
from .views import ItemsView

urlpatterns = [
    path('items/', ItemsView),
]