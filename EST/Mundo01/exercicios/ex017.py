
 # Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
import os
import time

catetoOposto = int(input('Entre com o comprimento do cateto oposto: '))
catetoAdjacente = int(input('Entre com o comprimento do cateto adjacente: ' ))

hipotenusa = math.hypot(catetoOposto,catetoAdjacente)

print('A hipotenusa é {}°'.format(math.ceil(hipotenusa)))
time.sleep(5)
os.system('clear') or None
