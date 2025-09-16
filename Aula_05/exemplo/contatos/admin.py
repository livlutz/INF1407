from django.contrib import admin
from contatos.models import Pessoa
from contatos.models import Endereco

# Register your models here.
#superuser : email da puc - 1

admin.site.register(Pessoa)
admin.site.register(Endereco)