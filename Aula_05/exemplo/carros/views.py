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


class CarView(APIView):

    @swagger_auto_schema(
        operation_summary ='Criar carro', operation_description="Criar um novo carro",
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'name': openapi.Schema(default='Honda HRV 2021', description='Modelo do carro', type=openapi.TYPE_STRING,),
                'mpg': openapi.Schema(default=24.85, description='Milhas por galão', type=openapi.TYPE_NUMBER,),
                'cyl': openapi.Schema(default=4, description='Quantidade de cilindros', type=openapi.TYPE_INTEGER),
                'disp': openapi.Schema(default=1.8, description='Volume do motor', type=openapi.TYPE_NUMBER),
                'hp': openapi.Schema(default=140, description='Potência em HP', type=openapi.TYPE_INTEGER),
                'wt': openapi.Schema(default=2.87686, description='Peso em 1000 libras', type=openapi.TYPE_NUMBER),
                'qsec': openapi.Schema(default=11.88, description='Tempo para percorrer 1/4 milha', type=openapi.TYPE_NUMBER),
                'vs': openapi.Schema(default=0, description='Motor em V ou em linha (straight) (0=v, 1=s)', type=openapi.TYPE_INTEGER),
                'am': openapi.Schema(default=0, description='Transmissão (0=automática, 1=manual)', type=openapi.TYPE_INTEGER),
                'gear': openapi.Schema(default=7, description='Número de marchas para frente', type=openapi.TYPE_INTEGER),
            },
        ),
        responses = {
            201: MTCarsSerializer,
            400: 'Dados errados',
        },
        manual_parameters = [
            openapi.Parameter('id_arg', openapi.IN_PATH,default=5,type=openapi.TYPE_INTEGER,required=True, description='ID do carro na URL'),
        ],
    )

    def post(self,request):
        serializer = MTCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id_arg):
        '''id_arg é o mesmo nome que colocamos em urls.py'''
        """
        Retorna um carro específico pelo id
        Lmebrar que o id vem pelo URL
        """
        queryset = self.singleCar(id_arg)
        if queryset:
            serializer = MTCarsSerializer(queryset)
            return Response(serializer.data)
        else:
            # o id na msg de erro deve ser apenas para depuração
            return Response({'msg': f'Carro com id #{id_arg} não existe'}, status=status.HTTP_400_BAD_REQUEST)

    def singleCar(self, id_arg):
        try:
            queryset = MTCars.objects.get(id=id_arg)
            return queryset
        except MTCars.DoesNotExist: # id não existe
            return None

    @swagger_auto_schema(
        operation_summary ='Atualizar carro', operation_description="Atualizar um carro existente",
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                'name': openapi.Schema(default='Honda HRV 2021', description='Modelo do carro', type=openapi.TYPE_STRING,),
                'mpg': openapi.Schema(default=24.85, description='Milhas por galão', type=openapi.TYPE_NUMBER,),
                'cyl': openapi.Schema(default=4, description='Quantidade de cilindros', type=openapi.TYPE_INTEGER),
                'disp': openapi.Schema(default=1.8, description='Volume do motor', type=openapi.TYPE_NUMBER),
                'hp': openapi.Schema(default=140, description='Potência em HP', type=openapi.TYPE_INTEGER),
                'wt': openapi.Schema(default=2.87686, description='Peso em 1000 libras', type=openapi.TYPE_NUMBER),
                'qsec': openapi.Schema(default=11.88, description='Tempo para percorrer 1/4 milha', type=openapi.TYPE_NUMBER),
                'vs': openapi.Schema(default=0, description='Motor em V ou em linha (straight) (0=v, 1=s)', type=openapi.TYPE_INTEGER),
                'am': openapi.Schema(default=0, description='Transmissão (0=automática, 1=manual)', type=openapi.TYPE_INTEGER),
                'gear': openapi.Schema(default=7, description='Número de marchas para frente', type=openapi.TYPE_INTEGER),
            },
        ),
        responses = {
            200: MTCarsSerializer(),
            400: MTCarsSerializer(),
        },
        manual_parameters = [
            openapi.Parameter('id_arg', openapi.IN_PATH,default=5,type=openapi.TYPE_INTEGER,required=True, description='ID do carro na URL'),
        ],
    )
    def put(self, request, id_arg):
        '''Atualiza um carro específico pelo id.
        Se o carro não existir, retorna erro 400.
        Lmebrar que o id_arg vem da URL e tem que ter o mesmo nome.'''

        carro = self.singleCar(id_arg)
        serializer = MTCarsSerializer(carro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)