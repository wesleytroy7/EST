# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# import math
from math import tan, sin,cos, radians
angulo = int(input('Entre com ângulo: '))

print('O seno de {} é {:.2f},\nO Cosseno de {} é {:.2f},\nA tangente de {} é {:.2f}'.format(angulo, sin(radians(angulo)), angulo, cos(radians(angulo)), angulo, tan(radians(angulo))))