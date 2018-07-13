from django.urls import path
from .views import listagem

urlpatterns = [
    path('', listagem, name='listagem_curriculos'),
]
