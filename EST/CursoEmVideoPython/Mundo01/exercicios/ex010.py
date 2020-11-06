"""
Pergunte quanto vc tem na carteira e mostre quanto é esse valor em dolar
u$$1.00 = R$5.60
"""

salario = float(input('Entre com quanto você temna carteira:R$ '))

print('R${:.2f} equivale a U$${:.2f}'.format(salario, (salario / 5.60)))