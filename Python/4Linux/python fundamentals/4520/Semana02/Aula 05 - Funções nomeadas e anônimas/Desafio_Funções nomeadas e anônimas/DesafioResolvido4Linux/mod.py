#!/usr/bin/python3
''' Desafio resolvido pela 4 linux'''

def abrindo_arquivo(arquivo: str) -> list: # O STR e uma notação apenas tonando claro que deve ser string e LIST que vai ser uma lista
    try:
        with open(arquivo, 'r') as arq:
            return arq.readlines()
    except Exception as erro:
        return ['Erro: {}'.format(erro)]
    


def escrevendo_no_arquivo(arquivo: str, conteudo: list) -> bool:
    try:
        with  open(arquivo, 'a') as arq:
            conteudo = [x + '\n' for x in conteudo]
            arq.writelines(conteudo)
            return True
    except Exception:
        return False


def contando_linhas(arquivo: str) -> int:
    return len(abrindo_arquivo(arquivo))