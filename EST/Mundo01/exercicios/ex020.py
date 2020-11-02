# o professor vai adicionar 4 alunos e quer que o programa mostre na tela a ordem de apresentação do trabalho
import random
import os
import time

listaOrdemAlunos = list(range(4))
i = 0
while i < len(listaOrdemAlunos):
    listaOrdemAlunos[i] = input('Entre  com o nome do aluno: ')
    i += 1
os.system('clear') or None
random.shuffle(listaOrdemAlunos)
# print(listaOrdemAlunos)
x = 0
print(50 * '-')
print('Ordem de apresentação será:')
while x <len(listaOrdemAlunos):
    print('{}º {}\n'.format(x+1,listaOrdemAlunos[x]))
    x += 1

time.sleep(5)
# os.system('clear') or None



   



