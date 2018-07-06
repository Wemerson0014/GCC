from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    biografia = models.TextField()
    pretensao_Salarial = models.DecimalField(max_digits=5, decimal_places=2)
    observacao = models.TextField()
    cargo = models.TextField()

