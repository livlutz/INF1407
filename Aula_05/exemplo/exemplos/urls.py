from django.urls import path
from exemplos import views

app_name = 'exemplos'

urlpatterns = [
    path('exemploClasse/', views.ExemploClasse.as_view(), name='exemploClasse'),
    path('exemploGET/', views.exemploGet, name='exemploGET'),
    path('exemploPOST/', views.exemploPost, name='exemploPOST'),
    path('exemploPUTDELETE/', views.exemploPutDelete, name='exemploPUTDELETE'),
]