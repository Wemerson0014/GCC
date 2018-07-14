from django import forms
from .models import candidato

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = candidato
        fields = ['nome', 'sobrenome', 'experiencias', 'cargo', 'pretensao_salarial', 'observacao']