"""
Leia um numero e mostre o dobro,triplo,raiz quadrada
"""
from math import sqrt
numero = int(input('Entre um numero: '))
dobro = numero * 2
triplo = numero * 3
raizquadrada = numero**(1/2)
raiz = sqrt(numero)

print('Dobro {}, Triplo {}, Raiz Quadrada {}, Raiz Exata {:.2f}'.format(dobro,triplo,raizquadrada,raiz))