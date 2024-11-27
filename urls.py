from django.urls import path
from gestao.views import minhas_atividades

from .views.funcionarioViews import registroViews, criacao_do_registro,\
dashboardFuncionario, login_create, criar_logout, FuncionarioUpdateViews
from gestao.views import criar_atividade, download_historico_pdf



app_name = 'autor'
urlpatterns = [
    path('registro/',registroViews , name='registro' ),
    path('registro/criacao/',criacao_do_registro , name='criacao' ),
    #path('login/',login_views , name='login' ),
    path('login/', login_create, name='cria_login',),
    path('logout/', criar_logout, name='logout',),
    path('atividade/', criar_atividade, name='sucesso',),
    path('perfil/',dashboardFuncionario, name='dashboard'),
    path('perfil/minhas-atividades/', minhas_atividades, name='minhas_atividades'),
    path('perfil/minhas-atividades/download-historico/', download_historico_pdf, name='download_historico'),
    path('funcionario/atualizar/',
         FuncionarioUpdateViews.as_view(), name='atualizar_fun'),
    
    
]
