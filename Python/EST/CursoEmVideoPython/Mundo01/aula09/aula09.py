import os,time
frase = 'Wesley & Suzan se AMAM, O SENHOR SÓ UNIU PARA SUA GLORIA!! s2'

sep = '=' *20
print(sep)
print(len(frase))
print(sep)
print(frase.count('a'))
print(sep)
print(frase.find('s'))
print(sep)
print(frase.isspace())
print(frase.rfind('S'))
print(frase.capitalize())
print(sep)
print(frase.lower().find('wesley'))
print('Lady' in frase)
print(sep)
print('W'in frase)
print(sep)
print(frase.find('W'))
print(frase[0:4])
time.sleep(5)
os.system('clear') or None