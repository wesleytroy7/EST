# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# import random
from random import shuffle
import os
import time

listaOrdemAlunos = list(range(4))
i = 0
while i < len(listaOrdemAlunos):
    listaOrdemAlunos[i] = input('Entre  com o nome do aluno: ')
    i += 1
os.system('clear') or None
shuffle(listaOrdemAlunos)
# print(listaOrdemAlunos)
x = 0
print(50 * '-')
print('Ordem de apresentação será:')
while x <len(listaOrdemAlunos):
    print('{}º {}\n'.format(x+1,listaOrdemAlunos[x]))
    x += 1

time.sleep(5)
# os.system('clear') or None



   



