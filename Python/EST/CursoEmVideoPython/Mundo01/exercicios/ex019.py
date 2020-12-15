#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# import random
from random import choice
import os
import time

lista = list(range(4))
i = 0
while i < len(lista):
    lista[i] = str(input('Entre com o nome:'))
    i +=1
print('Por favor {}, poderia apagar o quadro!'.format(choice(lista)))

time.sleep(3)
os.system('clear') or None