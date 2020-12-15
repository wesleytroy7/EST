#!/usr/bin/python3

linguagem = input('Qual  linguagem? ')

try:
    if linguagem.lower().strip() == 'python':
        print('vc acertou')
    else:
        raise ValueError('linguagem errada!!!')
except ValueError as erro:
    print('ERRO : {}'.format(erro))