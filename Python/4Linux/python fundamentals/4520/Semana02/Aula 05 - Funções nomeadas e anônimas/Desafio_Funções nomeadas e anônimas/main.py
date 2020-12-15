#!/usr/bin/python3

import Modulos.meu_modulo,os

os.system('clear')
Modulos.meu_modulo.ler_arquivo()

# escreva = (input('Escreva algo:')).split()
Modulos.meu_modulo.escrever_arquivo((input('Escreva algo:')).split())
Modulos.meu_modulo.ler_arquivo()

Modulos.meu_modulo.contar_linhas()