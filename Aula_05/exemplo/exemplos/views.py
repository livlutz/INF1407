from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

class ExemploClasse(APIView):
    def get(self,request):
        return Response(
            {
                "mensagem": "Olá, mundo!",
                "msg" : "mensagem via método GET"
            },
            status=status.HTTP_200_OK
        )

    def post(self,request):
        return Response(
            {
                "mensagem": "Olá, mundo!",
                "msg" : "mensagem via método POST"
            },
            status=status.HTTP_200_OK
        )

    def put(self,request):
        return Response(
            {
                "mensagem": "Olá, mundo!",
                "msg" : "mensagem via método PUT"
            },
            status=status.HTTP_200_OK
        )

    def delete(self,request):
        return Response(
            {
                "mensagem": "Olá, mundo!",
                "msg" : "mensagem via método DELETE"
            },
            status=status.HTTP_200_OK
        )

@api_view(('GET',)) #aqui tem que terminar com vírgula
@renderer_classes((JSONRenderer,))
def exemploGet(request):
    respostaJson = {
        "mensagem": "Olá, mundo!",
        "msg" : "mensagem via método GET da função"
    }
    return Response(
        respostaJson,
        status=status.HTTP_200_OK
    )

@api_view(('POST',))
def exemploPost(request):
    return Response(
        {
            "mensagem": "Olá, mundo!",
            "msg" : "mensagem via método POST da função"
        },
        status=status.HTTP_200_OK
    )

@api_view(('PUT','DELETE')) #aqui não precisa terminar com vírgula
def exemploPutDelete(request):
    return Response(
        {
            "mensagem": "Olá, mundo!",
            "msg" : "mensagem via método PUT ou DELETE da função"
        },
        status=status.HTTP_200_OK
    )
