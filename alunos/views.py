from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Aluno
from .forms import AlunoForm


class HomeView(FormView):

    template_name = "alunos/aluno_form.html"
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form: AlunoForm):
        messages.success(self.request, 'Cadastrado com sucesso.')
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Corrige os erros e tente novamente.')
        return super().form_invalid(form)


def sobre(request):
    return render(request, 'alunos/sobre.html')