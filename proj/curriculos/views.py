from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import candidato
from .forms import CandidatoForm

@login_required
def listagem(request):
    candidatos = candidato.objects.all()
    return render(request, 'curriculos.html', {'candidatos': candidatos})


@login_required
def novo(request):
    form = CandidatoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem_curriculos')

    return render(request, 'candidato-form.html', {'form': form})


@login_required
def atualizar(request, id):
    candidatos = candidato.objects.get(id=id)
    form = CandidatoForm(request.POST or None, instance=candidatos)

    if form.is_valid():
        form.save()
        return redirect('listagem_curriculos')

    return render(request, 'candidato-form.html', {'form': form, 'candidatos': candidatos})


@login_required
def deletar(request, id):
    candidatos = candidato.objects.get(id=id)

    if request.method == 'POST':
        candidatos.delete()
        return redirect('listagem_curriculos')

    return render(request, 'candidato-deletar.html', {'candidatos': candidatos})



