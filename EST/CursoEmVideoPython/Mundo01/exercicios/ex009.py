"""
Leia um numero inteiro e mostre na tela sua tabuada
"""

tabuada = int(input('Entre com um numero e vou mostrar a tabuada: '))

for x in range(1,11):
    print('{} x {:28} = {}'.format(tabuada, x, (tabuada*x)))

