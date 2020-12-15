#!/usr/bin/python3

# menu = True
def  opcao_A():
    return 'A'

def opcao_B():
    return 'B'

def opcao_C():
    pass

opcao = input("")

# while True: # menu == True
#     print(f"Escolha a opcao desejada:\n"
#            f"1- Opcao  A\n"
#            f"1- Opcao  B\n"
#            f"1- Opcao  C\n"
#            f"4- Sair")
while True: # menu == True
    print(f"Escolha a opcao desejada:\n"
           f"1- Opcao  A\n"
           f"1- Opcao  B\n"
           f"1- Opcao  C\n"
           f"4- Sair")

dic = {
    '1': opcao_A,
    '2': opcao_B,
    '3': opcao_C
}

try:
    print(dic[opcao])

except KeyError as e:
    print('Digite uma opcao válida')
except Exception as e:
    print(f'Erro desconhecido')
else:
    print('Ocorreu tudo bem')
finally:
    print('Retornando ao menu pricipal')



