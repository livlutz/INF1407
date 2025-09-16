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

class Endereco(models.Model):
     id = models.AutoField(primary_key=True)
     pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, related_name='enderecos')
     logradouro = models.CharField(max_length=200,help_text="Logradouro")
     numero = models.CharField(max_length=10, help_text = "Número")
     complemento = models.CharField(max_length=50,blank=True,null=True, help_text="complemento")
     bairro = models.CharField(max_length=100, help_text = "Bairro")
     cidade = models.CharField(max_length=100, help_text = "Cidade")
     estado = models.CharField(max_length=2, help_text = "Estado")
     cep = models.CharField(max_length=100, help_text = "CEP")

     def __str__(self):
        return f"{self.pessoa} : {self.logradouro}, {self.numero}, {self.complemento}, {self.bairro}, {self.cidade}, {self.estado}, {self.cep} "

