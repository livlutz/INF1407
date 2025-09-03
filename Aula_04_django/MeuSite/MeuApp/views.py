from django.shortcuts import render
from django.http import HttpResponse
#classe tem sempre letra maiúscula

# Create your views here.
def home(request):
    return render(request, 'MeuApp/home.html')

def stellar_evolution(request):
    return render(request, 'MeuApp/stellar_evolution.html')

def expansion(request):
    return render(request, 'MeuApp/expansion.html')

def particles(request):
    return render(request, 'MeuApp/particles.html')

def space_missions(request):
    return render(request, 'MeuApp/space_missions.html')

