#!/usr//bin/python3

produtos = [
        {'nome': 'prod01', 'valor': 2.0},
        {'nome': 'prod02', 'valor': 3.0},
        {'nome': 'prod03', 'valor': 2.89}
]

try:
    for produto in produtos:
        produto['valor'] += produto['valor'] * 0.1
except KeyError as erro:
    print('chave não pertence\
        ao produto: {}'.format(erro))
except Exception as errogenerico:
    print('Erro generico{}'.format(errogenerico))
finally:
    print(produtos)

    





