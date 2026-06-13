from django import forms
from .models import Aluno
from .validators import validar_cpf


class CodigoForm(forms.Form):
    codigo = forms.CharField(
        label='Código',
        max_length=20,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Digite o código...'})
    )


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['codigo', 'nome', 'cpf', 'idade']

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        validar_cpf(cpf)
        return cpf