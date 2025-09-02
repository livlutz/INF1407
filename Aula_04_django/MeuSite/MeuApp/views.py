from django.shortcuts import render
from django.http import HttpResponse
#classe tem sempre letra maiúscula

# Create your views here.
def home(request):
    return render(request, 'MeuApp/home.html')

def segunda(request):
    return render(request, 'MeuApp/segundaPagina.html')
