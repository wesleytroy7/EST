
 # Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
import os
import time

catetoOposto = int(input('Entre com o comprimento do cateto oposto: '))
catetoAdjacente = int(input('Entre com o comprimento do cateto adjacente: ' ))

hipotenusa = math.hypot(catetoOposto,catetoAdjacente)

#Maneira matematica
hi = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print('A hipotenusa é {}°'.format(math.ceil(hipotenusa)))

print(50 * '-')
print('A hipotenusa é {:.0f}º'.format(hi))
time.sleep(5)
os.system('clear') or None
