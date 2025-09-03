from django.shortcuts import render
from django.http import HttpResponse
#classe tem sempre letra maiúscula

# Create your views here.
def home(request):
    return render(request, 'MeuApp/home.html')

def stellar_evolution(request):
    return render(request, 'MeuApp/stellar_evolution.html')

def solar_system(request):
    return render(request, 'MeuApp/solar_system.html')

def galaxies(request):
    return render(request, 'MeuApp/galaxies.html')

def space_missions(request):
    return render(request, 'MeuApp/space_missions.html')

