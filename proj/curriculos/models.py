from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length=50, default='')
    sobrenome = models.CharField(max_length=50, default='')
    experiencias = models.TextField(default='')
    cargo = models.TextField(default='')
    pretensao_salarial = models.DecimalField(max_digits=6, decimal_places=3)
    observacao = models.TextField(default='')


    def __str__(self):
        return self.nome





