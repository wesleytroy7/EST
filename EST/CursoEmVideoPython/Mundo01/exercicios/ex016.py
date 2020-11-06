# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# import math 
from math import trunc
numero = float(input('Entre com um numero:\n'))

# Primeira forma
print('{} tem a porção inteira igual à {}'.format(numero, trunc(numero))) # trunc corta a parte inteira do numero

# Segunda forma 
print('{} tem a porção inteira igual à {}'.format(numero, int(numero) ))
