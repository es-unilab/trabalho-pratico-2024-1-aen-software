from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from autor.forms.login_form import LoginForms
from .models import Atividade, TipoEnsino, Graducao, PosGraduacao, Pesquisa
from .forms import AtividadeForm, TipoEnsinoForm, GraducaoForm, PosGraduacaoForm, PesquisaForm
from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse


def home(request):
    form = LoginForms()
    return render(request, 'gestao/pages/home.html', context={
        'login_form': form,
        'form_action_login': reverse('autor:cria_login')
    })

def litar(request):
    funcionario = User.objects.all()
    return render(request,'gestao/pages/pesquisa.html',context={
        'funcionarios':funcionario
    })
def criar_atividade(request):
    if request.method == 'POST':
        atividade_form = AtividadeForm(request.POST)
        tipo_ensino_form = TipoEnsinoForm(request.POST)
        graduacao_form = GraducaoForm(request.POST)
        pos_graduacao_form = PosGraduacaoForm(request.POST)
        pesquisa_form = PesquisaForm(request.POST)

        if atividade_form.is_valid():
            atividade = atividade_form.save(commit=False)
            atividade.usuario = request.user
            atividade.save()

            if tipo_ensino_form.is_valid():
                tipo_ensino = tipo_ensino_form.save(commit=False)
                tipo_ensino.atividade = atividade
                tipo_ensino.save()

                # Vincular Graduação
                if graduacao_form.is_valid():
                    graduacao = graduacao_form.save(commit=False)
                    graduacao.tipo_ensino = tipo_ensino
                    graduacao.save()

                # Vincular Pós-Graduação
                if pos_graduacao_form.is_valid():
                    pos_graduacao = pos_graduacao_form.save(commit=False)
                    pos_graduacao.tipo_ensino = tipo_ensino
                    pos_graduacao.save()

                # Vincular Pesquisa
                if pesquisa_form.is_valid():
                    pesquisa = pesquisa_form.save(commit=False)
                    pesquisa.tipo_ensino = tipo_ensino
                    pesquisa.save()

            return redirect(reverse('autor:minhas_atividades'))
        else:
            messages.error(request, "Erro ao salvar a atividade. Verifique os dados e tente novamente.")

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
    }
    return render(request, 'gestao/pages/criar_atividades.html', context)

def minhas_atividades(request):
    # Filtra todas as atividades associadas ao autor logado (usuario)
    atividades = Atividade.objects.filter(usuario=request.user).prefetch_related(
        'tipos_ensino__graduacao_opcoes',
        'tipos_ensino__pos_graduacao_opcoes',
        'tipos_ensino__pesquisa_opcoes',
    )

    context = {
        'atividades': atividades,
    }
    
    return render(request, 'gestao/pages/minhas_atividades.html', context)




def download_historico_pdf(request):
    # Verifica se o usuário está autenticado
    if not request.user.is_authenticated:
        return HttpResponse('Você precisa estar logado para acessar este recurso.', status=403)
    # Pega todas as atividades associadas ao usuário logado
    atividades = request.user.atividades.all()
    # Gera o contexto para o template
    context = {
        'atividades': atividades,
        'user': request.user,
    }
    # Renderiza o HTML do template com o contexto
    template = 'gestao/pages/minhas_atividades.html'  # Substitua com o caminho correto para o seu template
    html = render_to_string(template, context)
    # Cria a resposta HTTP para gerar o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="historico_atividades_{request.user.first_name}.pdf"'
    # Converte o HTML para PDF
    pisa_status = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=response)
    # Se houver erro ao gerar o PDF, retorna uma mensagem de erro
    if pisa_status.err:
        return HttpResponse('Erro ao gerar PDF', status=400)

    return response

    
def editar_atividade(request):

    atividade = Atividade.objects.filter(pk=id, autor=request.user)
    pass
    

def pesquisa_funcinario(request):
    termo_pesquisa = request.GET.get('search','')
    if not termo_pesquisa:
        raise Http404
    pesquisa = Q (
        Q(username__icontains=termo_pesquisa) |
        Q(first_name__icontains=termo_pesquisa), 
    )

    
    return render(request,'gestao/pages/pesquisa.html', context={
        'page_title': f'Search for "{pesquisa}" |',
        'termo_pesquisa': pesquisa,
        'additional_url_query': f'&search={pesquisa}',
    })


