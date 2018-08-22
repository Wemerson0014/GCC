from django.urls import path
from .views import home, sair


urlpatterns = [
    path('', home, name='home'),
    path('logout/', sair, name='logout'),
]


