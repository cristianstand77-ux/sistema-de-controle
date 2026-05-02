from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    idade = models.IntegerField()
    entrada = models.DateTimeField()
    saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome
