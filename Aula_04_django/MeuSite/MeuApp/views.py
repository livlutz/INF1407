from django.shortcuts import render
from django.http import HttpResponse
#classe tem sempre letra maiúscula

# Create your views here.
def home(request):
    return HttpResponse("Hello, world!")
