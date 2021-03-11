from django.urls import path
from .views import index, saludos

urlpatterns = [
    path('', index),
    path('saludos/', saludos),
]
