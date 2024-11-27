from django import forms
from ..models import Atividade, TipoEnsino, Graducao, PosGraduacao, Pesquisa

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['nome']

    nome = forms.ChoiceField(
        choices=[
            ('selecione uma atividade', 'Selecione uma atividade'),
            ('Ensino', 'Ensino'),
            ('Pesquisa', 'Pesquisa'),
            ('Extensão', 'Extensão'),
            ('Gestão', 'Gestão'),
        ],
        widget=forms.Select(attrs={
            'class': 'select_font form-control',
            'name': 'nome',
            'id': 'atividade',
        }),
        label='Escolha a atividade'
    )


class TipoEnsinoForm(forms.ModelForm):
    class Meta:
        model = TipoEnsino
        fields = ['nome']

        widgets={
            'nome': forms.Select(choices=(
                ('selecione o tipo de ensino','selecione o tipo de ensino'),
                ('graduacao','Graduação'),
                ('pos_graduacao','Pós-Graduação'),
                
                ),
                attrs={
                    'class':"form-control tipo_ensino select_font",
                    'name':'tipo_ensino',
                    'id':'tipo_ensino',
                    
                }
            )
            
        }
        labels ={
            'nome':'Tipo de ensino'
        }

class GraducaoForm(forms.ModelForm):
    class Meta:
        model = Graducao
        fields = ['aula', 'orientacao', 'monitoria', 'carga_horaria_min', 'carga_horaria_max']
        widgets = {
            'sala': forms.CheckboxInput(attrs={
                'name':'sala',
                'class':'form-control'
            }),

            'orientacao': forms.CheckboxInput(attrs={
                'name':'orientacao',
            }),

            'monitoria': forms.CheckboxInput(attrs={
                'name':'monitoria', 
            }),
            'carga_horaria_min': forms.NumberInput(attrs={
                'class':'form-control carga_h',
                "name":"carga_horaria_min_graduacao",
                "id":"carga_horaria_min_graduacao",
                'for':'carga_horaria_min_graduacao'
            }),
            'carga_horaria_max': forms.NumberInput(attrs={
                'class':'form-control carga_h',
                "name":"carga_horaria_max_graduacao",
                "id":"carga_horaria_max_graduacao",
                'for':'carga_horaria_max_graduacao'
            }),
            
            }
        

class PosGraduacaoForm(forms.ModelForm):
    class Meta:
        model = PosGraduacao
        fields = ['atividade_mestrado', 'aula_mestrado', 'carga_horaria_min', 'carga_horaria_max']
        widgets = {
            'atividade_mestrado': forms.CheckboxInput(attrs={
                'name':'atividade_mestrado',
                
            }),

            'aula_mestrado': forms.CheckboxInput(attrs={
                'name':'aula_mestrado', 
            }),
            'carga_horaria_min': forms.NumberInput(attrs={
                'class':'form-control carga_h',
                "name":"carga_horaria_min_pos_graduacao", 
                "id":"carga_horaria_min_pos_graduacao"
            }),
            'carga_horaria_max': forms.NumberInput(attrs={
                'class':'form-control carga_h',
                "name":"carga_horaria_max_pos_graduacao", 
                "id":"carga_horaria_max_pos_graduacao",
            }),
            
            }


class PesquisaForm(forms.ModelForm):
    class Meta:
        model = Pesquisa
        fields = ['curso_pesquisa', 'eventos_pesquisa', 'orientacao', 'carga_horaria_min', 'carga_horaria_max']
        widgets = {
            'curso_pesquisa': forms.CheckboxInput(attrs={
                'name':'curso_pesquisa',
                
            }),

            'eventos_pesquisa': forms.CheckboxInput(attrs={
                'name':'eventos_pesquisa', 
            }),
            'orientacao': forms.CheckboxInput(attrs={
                'name':'Orientação', 
            }),
            'carga_horaria_min': forms.NumberInput(attrs={
                'class':'form-control carga_h',
                "name":"carga_horaria_min_pesquisa", 
                "id":"carga_horaria_min_pesquisa"
            }),
            'carga_horaria_max': forms.NumberInput(attrs={
                'class':'form-control carga_h',
                "name":"carga_horaria_max_pesquisa", 
                "id":"carga_horaria_max_pesquisa"
            }),
            
            }

