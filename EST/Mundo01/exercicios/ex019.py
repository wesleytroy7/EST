# sortear um dos quatros alunos para apagar o quadro, lendo o nome dele e escrendo na tela
import random
import os
import time

lista = list(range(4))
i = 0
while i < len(lista):
    lista[i] = input('Entre com o nome:')
    i +=1
print('Por favor {}, poderia apagar o quadro!'.format(random.choice(lista)))

time.sleep(3)
os.system('clear') or None