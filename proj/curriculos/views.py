from django.shortcuts import render, redirect
from .models import candidato
from .forms import CandidatoForm

def listagem(request):
    candidatos = candidato.objects.all()
    return render(request, 'curriculos.html', {'candidatos': candidatos})


def novo(request):
    form = CandidatoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem_curriculos')

    return render(request, 'candidato-form.html', {'form': form})


def atualizar(request, id):
    candidatos = candidato.objects.get(id=id)
    form = CandidatoForm(request.POST or None, instance=candidato)

    if form.is_valid():
        form.save()
        return redirect('listagem_curriculos')

    return render(request, 'candidato-form.html', {'form': form, 'candidato': candidato})


def deletar(request, id):
    candidatos = candidato.objects.get(id=id)

    if request.method == 'POST':
        candidatos.delete()
        return redirect('listagem_curriculos')

    return render(request, 'candidato-deletar.html', {'candidato': candidato})



