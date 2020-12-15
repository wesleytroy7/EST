#!/usr/bin/python3

# w = write  abre para escrita e sobrescreve
# r = read somente leitura
#  x = abre para criação (falha caso o arquivo exista)
# a = abre para escrita e acrecenta no arquivo
#  +  = abre um arquivo para atualizalção leitura e escrita
#  
# arquivo = open('frutas.txt', 'w')
# arquivo.write('mamao')
# arquivo.close()

# with open('frutas.txt', 'w') as arquivo:
#     arquivo.write('manga\n')
#     arquivo.write('abacate\n')

# with open('frutas.txt', 'r') as arquivo:
    # print(arquivo.read())
    # print(type(arquivo.read()))
    # print(arquivo.readlines())
    # print(type(arquivo.readlines())

nomes = [ 'joad', 'giumar', 'wrere']

with open('nomes.txt', 'w') as arquivo:
    for nome in nomes:
        arquivo.write(nome + '\n')