from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    experiencias = models.TextField()
    cargo = models.TextField()
    pretensao_salarial = models.DecimalField(max_digits=6, decimal_places=3)
    observacao = models.TextField()


    def __str__(self):
        return self.nome





