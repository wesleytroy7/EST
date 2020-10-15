"""
Leia duas notas e caucule a média
"""
from statistics import median
n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))

media = (n1 + n2) / 2
media2 = [n1, n2]
print('A média é {}'.format(media))
print('Media estatistica {}'.format(median(media2)))