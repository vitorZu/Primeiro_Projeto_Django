from django.urls import path
from django.contrib import admin
from pages.views import IndexView, RegisterView, Store


urlpatterns = [
    path('', IndexView.as_view(), name = 'login'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('store/', Store),
    # path('', IndexView),
    # path('register/', RegisterView),
]