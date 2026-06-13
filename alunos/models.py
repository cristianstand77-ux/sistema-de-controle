from django.db import models


class Aluno(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    idade = models.IntegerField()

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Registro(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='registros')
    entrada = models.DateTimeField(auto_now_add=True)
    saida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.aluno.codigo} - {self.entrada}"

    class Meta:
        ordering = ['-entrada']