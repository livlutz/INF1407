"""
docstring com palavras chaves (ex @author)
"""
import math
#dicionário
# par chave: valor
"""switcher = {
    'A': cadastrar,
    'B': editar,
    'C': apagar,
    'D': listar,
    'Z': sair,
}

#ou
dicionario = dict()
dicionario.get(chave,valor)

switcher.get(opcao, lambda: print("opção inválida"))"""

#def funcao(v1):
    #""" texto de documentação -> colocar no trabalho"""
    #return

"""
Função lambda é uma função anônima com referência a outra função
"""

#def main():
    #return

#if __name__ == "__main__":
    #main()

#nome da classe começa com upper case por conveção
class NomeDaClasse:
    """Documentação da classe"""
    #atributos
    atr = ValueError
    #métodos
    #self é equivalente ao this em java
    def metodo(self,param): return

class Aluno:
    tipo = 'humano' #atributo da classe
    def __init__(self,nome):
        self.nome = nome #atributo de instância

al1=Aluno('João') #chama o construtor __init__
#acessar o atributo
print(al1.nome)

class Ponto:
    """se x e y não forem especificados, assumem o valor de 0 por default"""
    #métodos tem q ter o parâmetro self
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        return

    def __str__(self):
        return f'({self.x},{self.y})'

#não precisa chamar self na chamada do método
p1 = Ponto() #x = 0, y = 0
p2 = Ponto(3,4) # x = 3, y = 4
p3 = Ponto(3) # x = 3, y = 0
p4 = Ponto(y=4) # x = 0, y = 4
p5 = Ponto(y=4,x=5) # x = 5, y = 4

print(p5.__str__())

def funcao1(x,*argv):
    return

def funcao2(x,**kwargs):
    return

def funcao3(x,y,*argv,**kwargs):
    return

#dicionário vai para kwargs e argumentos adicionais vão para o argv