from django.urls import path, include
from carros import views
from rest_framework import routers, permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as yasg_schema_view
from drf_yasg import openapi

schema_view = yasg_schema_view(
    openapi.Info(
        title="API de Exemplo",
        default_version='v1',
        description="Descrição da API de exemplo",
        contact=openapi.Contact(email="llutz@aluno.puc-rio.br"),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url = 'https://cautious-enigma-76rxwrgqv5g3rr7v-8000.app.github.dev/carros/',
)

app_name = 'carros'

urlpatterns = [
    path("lista/", views.CarsView.as_view(), name="lista-carros"),
    path("umcarro/", views.CarView.as_view(), name="um-carro"),
    path('umcarro/<int:id_arg>/', views.CarView.as_view(), name='consulta-carro'),

    #URLs para o swagger
    path('docs/', include_docs_urls(title='Documentação da API Carros')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include(routers.DefaultRouter().urls)),
    path('openapi', get_schema_view(title="API para Carros", description="API para obter dados dos carros",), name='openapi-schema'),
]