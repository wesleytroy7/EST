""" Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome. """

import os
import time

nomeCompleto = str(input('Entre com o nome completo: ')).strip()
print(nomeCompleto)
print('Seu nome com todas letras Maisculas : {}'.format(str.upper(nomeCompleto)))
print('Seu nome em minusculo {}'.format(str.lower(nomeCompleto)))
print('{}'.format(len(nomeCompleto) - nomeCompleto.count(' ')))



time.sleep(5)
os.system('clear') or None