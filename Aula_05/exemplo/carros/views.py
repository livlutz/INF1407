from django.shortcuts import render
from carros.serializers import MTCarsSerializer
from rest_framework.views import APIView
from carros.models import MTCars
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
#curl -X GET http://localhost:8000/carros/lista/

class CarsView(APIView):
    @swagger_auto_schema(
        operation_summary='Lista todos os carros',
        operation_description=
        '''
        Retorna a lista de carros do banco de dados MTCars
        Essa lista é retornada em ordem alfabética
        pelo nome do carro.
        ''',
        request_body=None, # opcional -> passar o id do carro, por exemplo
        responses = {
            200: MTCarsSerializer,
        },
        url = 'https://cautious-enigma-76rxwrgqv5g3rr7v-8000.app.github.dev/carros/lista/'
    )

    def get(self,request):
        #name : nome python
        #NAME : nome no banco de dados
        queryset = MTCars.objects.all().order_by('name')
        #serializando os dados
        #carros: queryset do django
        #many=true vários objetos
        serializer = MTCarsSerializer(queryset, many=True)
        #retornando a resposta
        return Response(serializer.data, status=status.HTTP_200_OK)