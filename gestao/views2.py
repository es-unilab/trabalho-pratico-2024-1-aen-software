from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from autor.forms.login_form import LoginForms
from .models import Atividade, TipoEnsino, Graducao, PosGraduacao, Pesquisa
from .forms import AtividadeForm, TipoEnsinoForm, GraducaoForm, PosGraduacaoForm, PesquisaForm


def home(request):
    form = LoginForms()
    return render(request, 'gestao/pages/home.html', context={
        'login_form': form,
        'form_action_login': reverse('autor:cria_login')
    })

def criar_atividade(request):
    total_carga_min = 0
    total_carga_max = 0
    if request.method == 'POST':
        atividade_form = AtividadeForm(request.POST)
        tipo_ensino_form = TipoEnsinoForm(request.POST)
        graduacao_form = GraducaoForm(request.POST)
        pos_graduacao_form = PosGraduacaoForm(request.POST)
        pesquisa_form = PesquisaForm(request.POST)

        if atividade_form.is_valid():
            atividade = atividade_form.save()

        if tipo_ensino_form.is_valid():
            tipo_ensino = tipo_ensino_form.save()

        if graduacao_form.is_valid():
            graduacao = graduacao_form.save()

        if pos_graduacao_form.is_valid():
            pos_graduacao = pos_graduacao_form.save()

        if pesquisa_form.is_valid():
            pesquisa = pesquisa_form.save()

        return redirect(reverse('autor:sucesso'))
    
    else:
        atividade_form = AtividadeForm()
        tipo_ensino_form = TipoEnsinoForm()
        graduacao_form = GraducaoForm()
        pos_graduacao_form = PosGraduacaoForm()
        pesquisa_form = PesquisaForm()

    context = {
        'atividade_form': atividade_form,
        'tipo_ensino_form': tipo_ensino_form,
        'graduacao_form': graduacao_form,
        'pos_graduacao_form': pos_graduacao_form,
        'pesquisa_form': pesquisa_form,
        'total_carga_min': total_carga_min,
        'total_carga_max': total_carga_max
    }
    
    return render(request, 'gestao/pages/criar_atividades.html', context)



    
    