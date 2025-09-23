from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Renderiza a página inicial.
    """
    return render(request,"exemplo/home.html")


def homeSec(request):
    return render(request,"seguranca/homeSec.html")

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request,'seguranca/registro.html', context)

def logout(request):
    return render(request,'seguranca/logout.html')

@login_required
def paginaSecreta(request):

    """renderiza uma página secreta que requer autenticação"""

    return render(request,'privado/paginaSecreta.html')

#s12345678@ -> senha do usuario1