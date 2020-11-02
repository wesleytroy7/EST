# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = int(input('Entre com ângulo: '))

print('o Cosseno de {} é {:.3f}, a tangente de {} é {:.3f}'.format(angulo, math.cos(angulo), angulo, math.tan(angulo)))