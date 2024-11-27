from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Disciplina(models.Model):
    nome = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome

class Atividade(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="atividades", null=True, blank=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class TipoEnsino(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='tipos_ensino', null=True, blank=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Graducao(models.Model):
    tipo_ensino = models.ForeignKey(TipoEnsino, on_delete=models.CASCADE, related_name='graduacao_opcoes')
    aula = models.BooleanField(default=False)
    orientacao = models.BooleanField(default=False, blank=True)
    monitoria = models.BooleanField(default=False, blank=True)
    carga_horaria_min = models.PositiveIntegerField(blank=True)
    carga_horaria_max = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"Graduação ({self.tipo_ensino.nome})"

class PosGraduacao(models.Model):
    tipo_ensino = models.ForeignKey(TipoEnsino, on_delete=models.CASCADE, related_name='pos_graduacao_opcoes')
    atividade_mestrado = models.BooleanField(default=False, blank=True)
    aula_mestrado = models.BooleanField(default=False, blank=True)
    carga_horaria_min = models.PositiveIntegerField(blank=True)
    carga_horaria_max = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"Pós-Graduação ({self.tipo_ensino.nome})"

class Pesquisa(models.Model):
    tipo_ensino = models.ForeignKey(TipoEnsino, on_delete=models.CASCADE, related_name='pesquisa_opcoes', null=True)
    curso_pesquisa = models.CharField(max_length=100, blank=True)
    eventos_pesquisa = models.CharField(max_length=100, blank=True)
    orientacao = models.CharField(max_length=100, blank=True)
    carga_horaria_min = models.PositiveIntegerField(blank=True)
    carga_horaria_max = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"Pesquisa ({self.curso_pesquisa})"
