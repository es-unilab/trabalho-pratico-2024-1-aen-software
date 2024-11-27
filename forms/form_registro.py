from django import forms
from django.contrib.auth.models import User
BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
CARGO = {
    "professor": "professor",
    "funcionario administrativo": "funcionario administrativo",
}

class FormularioRegistro(forms.ModelForm):
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirma a senha',
        'label': 'confirmação',
        'class':'form-input form-control btn-password ',
        'name':'campoSenha',
        'id':'senha'
    }),
        required=True,
        error_messages={
            'required': 'A senha não deve ser diferente'},
        )
    data_nascimento = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES,attrs={
            'class':'form-control '
        })
    )
    tipo_funcionario = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs={
            'class':'m-2 '
        }),
        choices=CARGO,
        
    )
    
    class Meta:
        model = User

        fields = [
            'first_name', 
            'last_name',
            'username',
            'email',
            'password',
        ]
        labels = {
            'username': 'usuario',
            'first_name': 'nome',
            'last_name': 'sobrenome',
            'email': 'E-mail',
            'password': 'password',
            
        }
        
        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            
            },
            'password':{}
            }

        
        widgets ={
            'password': forms.PasswordInput(attrs={
                'placeholder':'digite a senha',
                'class':'form-control btn-password',
                'name':'campoSenha'
            }),
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'name':'username'
            }),
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control'
            }),
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            password_confirmation_error = forms.ValidationError(
                'Password devem ser iguais',
                code='invalid'
            )
            raise forms.ValidationError({
                
                'password': [
                    password_confirmation_error,
                ],
            })
    
    def clean_email(self):
        email= self.cleaned_data.get('email')
        existe = User.objects.filter(email=email).exists()
        if existe:
            raise(
                forms.ValidationError('email já existe:', code='invalid')
            )
        return email