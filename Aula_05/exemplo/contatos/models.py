from django.db import models

# Create your models here.

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)

    #help_text não vai para o db, isso vai para o formulário de preenchimento de dados
    nome = models.CharField(
        max_length=100, help_text='Entre o nome')

    idade = models.IntegerField(help_text='Entre a idade')

    salario = models.DecimalField(
        help_text='Entre o salário',
        decimal_places=2, max_digits=8)

    email = models.EmailField(
        help_text='Informe o email', max_length=254)

    telefone = models.CharField(
        help_text='Telefone com DDD e DDI', max_length=20)

    #verbose_name é o nome da variável que vai aparecer no formulário
    dtNasc = models.DateField(
        help_text='Nascimento no formato DD/MM/AAAA',
        verbose_name='Data de nascimento')

def __str__(self):
    return self.nome
