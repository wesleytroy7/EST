"""
Leia a largura, altura de uma parede em metros,
calcule sua área e a qtd de tinta necessária pra pintar,
sabendo que cada lintro de tinta pinta uma área de 2m²
"""
largura = float(input('Entre com a largura em metros: '))
altura  =  float(input('Entre com a altura em metros: '))

area = (largura * altura )
quantasLatas = (area / 2)

print('Sua parede tem aa dimensão de {}x{} e a área total é {:.3f}m² e é necessario {:.2f} litros de tinta para pintar'.format(largura, altura, area, quantasLatas))