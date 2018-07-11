from django.shortcuts import render
from .models import Candidato

def home (request):
    Candidatos = Candidato.objects.all()
    return render(request, 'curriculos.html')



