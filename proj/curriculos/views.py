from django.shortcuts import render, redirect
from .models import candidato
from .forms import CandidatoForm

def listagem (request):
    candidatos = candidato.objects.all()
    return render(request, 'curriculos.html', {'candidatos': candidato})

def novo (request):
    form = CandidatoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    return render(request, 'candidato-form.html', {'form': form})


