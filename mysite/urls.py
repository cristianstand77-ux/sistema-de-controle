from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from alunos.views import (
    HomeView,
    sobre,
    CoordenadorLoginView,
    coordenador_home,
    cadastrar_aluno,
    RegistrosListView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('sobre/', sobre, name='sobre'),

    path('login/', CoordenadorLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    path('coordenador/', coordenador_home, name='coordenador_home'),
    path('coordenador/cadastrar/', cadastrar_aluno, name='cadastrar_aluno'),
    path('coordenador/registros/', RegistrosListView.as_view(), name='registros_list'),
]