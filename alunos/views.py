from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView, ListView

from .models import Aluno, Registro
from .forms import AlunoForm, CodigoForm


class HomeView(FormView):
    """Tela pública da catraca: digita o código e registra entrada/saída."""
    template_name = "alunos/catraca.html"
    form_class = CodigoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        codigo = form.cleaned_data['codigo'].strip()

        try:
            aluno = Aluno.objects.get(codigo=codigo)
        except Aluno.DoesNotExist:
            messages.error(self.request, f'Código "{codigo}" não encontrado.')
            return super().form_valid(form)

        registro_aberto = aluno.registros.filter(saida__isnull=True).first()

        if registro_aberto:
            registro_aberto.saida = timezone.now()
            registro_aberto.save()
            messages.success(self.request, f'Saída registrada para {aluno.nome}.')
        else:
            Registro.objects.create(aluno=aluno)
            messages.success(self.request, f'Entrada registrada para {aluno.nome}.')

        return super().form_valid(form)


class CoordenadorLoginView(LoginView):
    template_name = 'alunos/login.html'
    redirect_authenticated_user = True


@login_required
def coordenador_home(request):
    return render(request, 'alunos/coordenador_home.html')


@login_required
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso.')
            return redirect('cadastrar_aluno')
        else:
            messages.error(request, 'Corrige os erros e tente novamente.')
    else:
        form = AlunoForm()

    return render(request, 'alunos/aluno_form.html', {'form': form})


class RegistrosListView(ListView):
    model = Registro
    template_name = 'alunos/registros_list.html'
    context_object_name = 'registros'
    paginate_by = 30

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


def sobre(request):
    return render(request, 'alunos/sobre.html')