from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['entrada'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['saida'].input_formats = ['%Y-%m-%dT%H:%M']

    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'idade', 'entrada', 'saida']

        widgets = {
            'entrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'saida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
