from django.urls import path
from .views import listagem, novo, atualizar, deletar

urlpatterns = [
    path('', listagem, name='listagem_curriculos'),
    path('novo/', novo, name='novo_curriculos'),
    path('atualizar/<int:id>/', atualizar, name='atualizar_curriculos'),
    path('deletar/<int:id>/', deletar, name='deletar_curriculos'),
]
