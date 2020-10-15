"""
     screva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
quilometrosPercorridos = float(input('Entre com a quantidade de Km  percorridos: '))
quantidadeDias = int(input('Entre com quantidade de dias: '))

totalDiaria  = 60 * quantidadeDias
totalValorKm = quilometrosPercorridos * 0.15

print('Total a pagar é : R${:.2f}'.format(totalDiaria + totalValorKm))

