from django.shortcuts import render
from carros.serializers import MTCarsSerializer
from rest_framework.views import APIView
from carros.models import MTCars
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#curl -X GET http://localhost:8000/carros/lista/

class CarsView(APIView):
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