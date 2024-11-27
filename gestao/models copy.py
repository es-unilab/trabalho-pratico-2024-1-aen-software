from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Regime(models.Model):
    descricao = models.CharField(max_length=60)
    carga_horario = models.PositiveIntegerField()

class Categoria_atividade:
    descricao = models.CharField(max_length=60)
    maximo = models.PositiveIntegerField()
    minimo = models.PositiveIntegerField()


class Tipo_atividade(models.Model):
    descricao = models.CharField(max_length=30)
    maximo = models.PositiveIntegerField()
    minimo = models.PositiveIntegerField()
    id_categoria = models.ForeignKey(Categoria_atividade, on_delete=models.CASCADE, null=True)

class Professor:
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    id_regime = models.ForeignKey(Regime, on_delete = models.CASCADE, null = True)

class Atividade2:
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    id_tipo_atividade = models.ForeignKey(Tipo_atividade, on_delete = models.CASCADE, null = True)
    descricao = models.CharField(max_length=100)
    carga_horaria = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data')



class Disciplina(models.Model):
    nome = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome

class Ministra(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    data_de_registro = models.DateTimeField(auto_now_add=True, verbose_name='Data de registro')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True)
    '''    def __str__(self):
        return self.usuario
    
    '''
# MODELAÇÃO DAS ATIVIDADES

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class TipoEnsino(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, related_name='tipos_ensino')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Graducao(models.Model):
    tipo_ensino = models.ForeignKey(TipoEnsino, on_delete=models.CASCADE, related_name='graduacao_opcoes')
    aula = models.BooleanField(default=False)
    orientacao = models.BooleanField(default=False)
    monitoria = models.BooleanField(default=False)
    carga_horaria_min = models.PositiveIntegerField()
    carga_horaria_max = models.PositiveIntegerField()

    def __str__(self):
        return f"Graduação ({self.tipo_ensino.nome})"


class PosGraduacao(models.Model):
    tipo_ensino = models.ForeignKey(TipoEnsino, on_delete=models.CASCADE, related_name='pos_graduacao_opcoes')
    atividade_mestrado = models.BooleanField(default=False)
    aula_mestrado = models.BooleanField(default=False)
    carga_horaria_min = models.PositiveIntegerField()
    carga_horaria_max = models.PositiveIntegerField()

    def __str__(self):
        return f"Pós-Graduação ({self.tipo_ensino.nome})"


class Pesquisa(models.Model):
    curso_pesquisa = models.CharField(max_length=100)
    eventos_pesquisa = models.CharField(max_length=100)
    orientacao = models.CharField(max_length=100)
    carga_horaria_min = models.PositiveIntegerField()
    carga_horaria_max = models.PositiveIntegerField()

    def __str__(self):
        return f"Pesquisa ({self.curso_pesquisa})"