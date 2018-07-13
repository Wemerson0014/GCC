from django.shortcuts import render
from .models import Candidato

def listagem (request):
    Candidatos = Candidato.objects.all()
    return render(request, 'curriculos.html', {'Candidatos': Candidato})




