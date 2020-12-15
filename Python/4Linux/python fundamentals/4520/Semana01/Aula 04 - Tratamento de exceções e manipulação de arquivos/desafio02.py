
#!/usr/bin/python3.8


# import os# importando o modulo do OS

# texto = 'texto'

# if (os.path.exists('/home/wesley/4Linux/python fundamentals/4520/des.txt')):
#    os.remove('/home/wesley/4Linux/python fundamentals/4520/des.txt')
#    doc = open('des.txt', 'x')#cria
#    with open('des.txt', 'w') as arquivo:# abre e escreve
#      arquivo.write('blabla')
#    arquivo.close()

#    with open('des.txt', 'r') as arquivo:# leitura
#         print(arquivo.read())
#         arquivo.close()

#    with open('des.txt', 'w') as arquivo:# escreve
#             for num in range(1,4):
#                arquivo.write('{}-{}'.format((num),(texto)))
#             arquivo.close()

#    with open('des.txt', 'w') as arquivo:#escreve 
#         for num in range(1,4):
#             arquivo.write('{}-{}\n'.format((num),(texto) ))

# abre em modo leitura
try:
    with open('des.txt', 'r') as arquivo:
    # contador = 1 # cria um contador
    # conteudo = [] # cria uma lista
    # for linha in arquivo:  # lê o arquivo e retona na linha 
    #     print(linha,'',arquivo)# aqui apenas retorna o que ocorre no for
    #     if (linha != '\n'):# aqui na linha somente fica o que não é linha vazia 
    #         print(contador)                     #0       1  só uma posição implicita     
    #         conteudo.append('{0}- {1}'.format(contador, linha))# adiciona o valor no comaeço da linha e guardando dentro da lista conteudo
    #         # print(conteudo,"contador",contador)
    #         contador += 1
    #---------------------------------------
    #OUTRA FORMA DE LOGICA
         conteudo = [(x) for (x) in (arquivo) if (x) != ('\n')]
         for x in range(len(conteudo)):
             conteudo[x] = '{}- {}'.format(x + 1, conteudo[x])
         print(conteudo)
    # -------------------------------------------
    with open('des.txt', 'w') as arquivo:# abre o arquivo e escreve nele o que está em memoria no conteudo
        # print("arquivo original ",arquivo)
        # print("conteudo ",conteudo)
        # print(type(conteudo))
        arquivo.writelines(conteudo)# o objeto  conteudo e uma lista , writelines recebe esse dado e escreve em arquivo, o writelines trabalha com lista e escreve linha por linha
        # print("arquivo pós rescrito",arquivo)
except FileNotFoundError:
    print('Arquivo não existe')
except Exception:
    print('Verifique!')
