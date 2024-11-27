from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs=
                                                     {'class':"form-control",
                                                    "placeholder":"usuario",
                                                    "name":"username"
                                                    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs=
                                                          {'class':"form-control",
                                                           "placeholder":"password",
                                                           "name":"campoSenha", "id":"senha"
                                                           }))
'''    
    class Meta:
        model = User
        fields = ['username','password']
'''