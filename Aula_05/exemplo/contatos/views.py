from django.shortcuts import render
from contatos.models import Pessoa
from django.views.generic.base import View

# Create your views here.

class ContatoListView(View):
    #argumento e dicionário de argumentos (args e kwargs)
    def get(self, request, *args, **kwargs):
        #recupera todas as pessoas do banco de dados
        pessoas = Pessoa.objects.all().order_by('nome')
        #contexto para o template (dicionário)
        #dicionário contexto
        #chave 'pessoas'
        #valor da chave é o objeto com todas as pessoas
        contexto = {'pessoas': pessoas}
        #lê,modifica e retorna o arquivo html
        return render(request, 'contatos/listaContatos.html',contexto)