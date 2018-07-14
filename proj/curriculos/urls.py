from django.urls import path
from .views import listagem, novo

urlpatterns = [
    path('', listagem, name='listagem_curriculos'),
    path('novo', novo, name='novo_curriculos'),
]
