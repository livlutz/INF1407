from django.shortcuts import render
from contatos.models import Pessoa
from contatos.models import Endereco
from django.views.generic.base import View
from contatos.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.shortcuts import render, get_object_or_404

# Create your views here.

class ContatoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = { 'formulario': ContatoModel2Form,
                    'titulo_janela' : 'Novo contato',
                    'titulo_pagina': 'Cadastra contato',
                    'botao' : 'Cadastrar',    }
        return render(request, "contatos/cadastroContato.html", contexto)

    def post(self,request,*arg,**kwargs):
        formulario = ContatoModel2Form(request.POST) #obtem o formulário preenchido
        if formulario.is_valid(): #valida o formulário
            contato = formulario.save() # salva o formulario no banco de dados
            contato.save()
            return HttpResponseRedirect(reverse_lazy ('contatos:lista-contatos'))
        else:
            contexto = {'formulario': formulario, 'mensagem': 'Erro ao salvar o contato!'}
            return render(request, "contatos/cadastroContato.html", contexto)

class ContatoListView(View):
    #argumento e dicionário de argumentos (args e kwargs)
    def get(self, request, *args, **kwargs):
        #recupera todas as pessoas do banco de dados
        pessoas = Pessoa.objects.all().order_by('nome')
        #contexto para o template (dicionário)
        #dicionário contexto
        #chave 'pessoas'
        #valor da chave é o objeto com todas as pessoas
        contexto = {'pessoas': pessoas,
                    'titulo_janela' : 'Lista contato',
                    'titulo_pagina': 'Lista contato',
                    'botao' : 'Listar'}
        #lê,modifica e retorna o arquivo html
        return render(request, 'contatos/listaContatos.html',contexto)

class ContatoUpdateView(View):
    '''
        classe para atualizar um contato
    '''
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk) # o primeiro pk é o parâmetro e o segundo é a primary key
        formulario = ContatoModel2Form(instance=pessoa)
        contexto = {
            'form': formulario,
            'titulo_janela' : 'Atualização de contato',
            'titulo_pagina': 'Atualiza contato',
            'botao' : 'Atualizar',
        }
        return render(request, 'contatos/formContato.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        form = ContatoModel2Form(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save() # cria uma pessoa com os dados do formulário
            pessoa.save() # salva uma pessoa no banco de dados
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        else:
            contexto = {'form': form, 'mensagem': 'Erro ao atualizar o contato!'}
            return render(request, 'contatos/formContato.html', contexto)

class ContatoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = { 'pessoa': pessoa,
                    'titulo_janela' : 'Deletar contato',
                    'titulo_pagina': 'Apagar contato',
                    'botao' : 'Deletar'}
        return render(request, 'contatos/confirmaExclusao.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))

class EnderecoListView(View):
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = {'enderecos': pessoa.enderecos.all(),
                    'titulo_janela' : 'Listar Enderecos',
                    'titulo_pagina': 'Listar Enderecos',
                    'botao' : 'Listar'}
        return render(request, 'contatos/listarEndereco.html', contexto)

