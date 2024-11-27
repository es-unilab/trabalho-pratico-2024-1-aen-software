from django.contrib import admin
from .models import Disciplina, Atividade, TipoEnsino, Graducao, PosGraduacao, Pesquisa
# Register your models here.

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(TipoEnsino)
class TipoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Graducao)
class GraduaacaoAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_ensino','aula','orientacao','monitoria')
    list_display_links = ('id','tipo_ensino','aula','orientacao','monitoria')
@admin.register(PosGraduacao)
class PosGraduaacaoAdmin(admin.ModelAdmin):
    list_display = ('id','tipo_ensino','atividade_mestrado','aula_mestrado',)
@admin.register(Pesquisa)
class PesquisaAdmin(admin.ModelAdmin):
    list_display = ('curso_pesquisa','eventos_pesquisa','orientacao')
    list_display_links = ('curso_pesquisa','eventos_pesquisa','orientacao')

