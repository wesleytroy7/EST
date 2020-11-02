"""
Leia o salario do funcionario e mostre o seu novo salario de 15% de aumento
"""
salario = float(input('Entre com seu salário: R$'))

print('Você recebeu um aumento de 15%, o seu salário é R${:.2f}'.format(salario + (salario * 15 / 100)))