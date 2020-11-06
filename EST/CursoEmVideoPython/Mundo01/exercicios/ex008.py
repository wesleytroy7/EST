"""
Leia um valor em metros e converta em centimetros e milimetros
"""
print('='*95)
print(' Quilometros |  Hectómetro |  Decâmetro  |  Metro  |  Decímetro  |  Centímetro  |  Milímetro\n')
print('    (Km)           (hm)          (dam)        (m)        (dm)          (cm)           (mm)' )
print('='*95)
valor = float(input('Entre com um valor em metros: '))

km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor *1000

print('{}km \n {}hm \n {}dam \n {:.0f}dm \n {:.0f}cm \n {:.0f}mm '.format(km, hm, dam, dm, cm, mm))