from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from autor.forms.form_registro import FormularioRegistro
from autor.forms.login_form import LoginForms
from django.http import Http404
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

def registroViews(request):
    
    form = FormularioRegistro()
    return render(request, 'gestao/pages/form.html', context={
        'form': form,
        'form_title': True,
        'form_action': reverse('autor:criacao')  # URL correta para o registro
    })

def criacao_do_registro(request):
    if request.method != 'POST':
        raise Http404
    POST = request.POST
    request.session['register_form_data'] = POST
    form = FormularioRegistro(POST, instance=request.User or None)
    
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)  # Criptografa a senha
        user.save()
        messages.success(request, 'Seu perfil foi criado com sucesso, faça o login.')
        del request.session['register_form_data']  # Remove dados da sessão
        return redirect(reverse('website:home'))
    
    messages.error(request, 'Verifique os erros nos campos abaixo.')
    return redirect(reverse('autor:registro'))


def login_create(request):
    if request.method != 'POST':
        raise Http404()
    form = LoginForms(request.POST)

    if form.is_valid():
        username = form.cleaned_data.get('username', '')
        password = form.cleaned_data.get('password', '')
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, 'Você está logado.')
            return redirect(reverse('autor:dashboard'))
        else:
            print(f'username= {username}, senha={password}')
            messages.error(request, 'Dados inválidos. Tente novamente.')
    else:
        messages.error(request, 'Erro no formulário. Verifique os dados.')

    return redirect(reverse('autor:dashboard'))  # Corrigido para redirecionar corretamente

@login_required(login_url='home', redirect_field_name='next')
def criar_logout(request):
    if request.user.is_authenticated:  # Verifica se o usuário está logado
        logout(request)
        messages.warning(request, 'Você foi desconectado. faça login')
    return redirect(reverse('website:home'))


def dashboardFuncionario(request):
    log ='log'
    if not request.user.is_authenticated:
        return redirect(reverse('website:home'))  # Verifica se o usuário está logado
    return render(request, 'gestao/pages/dashboard.html',context={
        'log':log
    })

# class de atualização do funcionario
class FuncionarioUpdateViews(UpdateView):
    template_name = 'gestao/pages/atualizar_func.html'
    model = User
    fields = [
        'id',
        'first_name',
        'last_name',
        'email',
        'password',
        
    ]

    def get_object(self, queryset=None):
        funcionario = None
        id = self.kwargs.get(self.pk_url_kwarg)
        # slug = self.kwargs.get(self.slug_url_kwarg)
        nome = self.request.POST.get('firs_name')
        if id is not None:
            funcionario = User.objects.filter(id=id).first()
            if nome is not None:
                messages.success(self.request, f'dados do funcionario {nome} atualizado') # noqa
        return funcionario
    success_url = reverse_lazy("autor:sucesso")
