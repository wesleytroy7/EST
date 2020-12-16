#!/usr/bin/python3

# criando um objeto

class Dog():
    '''Tentando abstrair um cachorro'''
    def __init__(self, nome, raca, idade): # self aponta para propria classe __init__ metodo contrutor que recebe inicializa e recebe os metodos
        self.nome = nome
        self.raca = raca
        self.idade = idade
    def latir(self):
        """
        docstring
        """
        pass
    def andar(self):
                """
        docstring
        """
        pass
    def comer(self):
       """
       docstring
       """
       pass

       
dog1 = Dog('Amora', 'lata', 4)

print(dog1.nome)
print(dog1.raca)
print(dog1.idade)

print(dir(dog1))