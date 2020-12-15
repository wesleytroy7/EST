#!/usr/bin/python3

def ler_arquivo():
   with open('/home/wesley/4Linux/python fundamentals/4520/Semana02/Aula 05 - Funções nomeadas e anônimas/Desafio_Funções nomeadas e anônimas/texto.txt', 'r') as leitura:
       print(leitura.readlines())
  
def escrever_arquivo(escrever):
    with open('/home/wesley/4Linux/python fundamentals/4520/Semana02/Aula 05 - Funções nomeadas e anônimas/Desafio_Funções nomeadas e anônimas/texto.txt', 'a',newline='\n') as escrita:
        escrita.writelines(escrever)
        
def contar_linhas():
    with open('/home/wesley/4Linux/python fundamentals/4520/Semana02/Aula 05 - Funções nomeadas e anônimas/Desafio_Funções nomeadas e anônimas/texto.txt', 'r') as contando:
        # total = sum(1 for linhas in contando) 
        # print(total)
        print(sum( 1 for i in contando))
    

