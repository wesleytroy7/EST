"""
Leia um preço e mostre seu novo preço  com 5% de desconto
"""

valorProduto = float(input('Entre com o valor do produto: R$'))

print('Você ganhou 5% de desconto :D , o valor total a pagar é {:.2f}'.format(valorProduto -(valorProduto * 5 / 100)))