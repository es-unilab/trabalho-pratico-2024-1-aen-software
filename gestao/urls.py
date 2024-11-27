from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('',views.home, name='home' ),
    path('inicio/',views.home, name='home' ),    
    path('inicio/funcionario/pesquisa/', views.pesquisa_funcinario, name='pesquisa' ),  # noqa  
    path('inicio/funcionario/lista/', views.litar, name='lista' ),  # noqa  
      
    
]