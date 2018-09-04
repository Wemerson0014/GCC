from django import forms
from .models import Candidato

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'sobrenome', 'experiencias', 'cargo', 'pretensao_salarial', 'observacao']