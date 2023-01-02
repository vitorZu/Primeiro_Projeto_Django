from django.urls import path
from .views import IndexView, RegisterView


urlpatterns = [
    path('', IndexView.as_view(), name = 'login'),
    path('register/', RegisterView.as_view(), name = 'register'),
]