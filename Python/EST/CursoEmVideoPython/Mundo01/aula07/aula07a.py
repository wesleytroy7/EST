nome = input('Qual é o seu nome? ')
print('Prazer {}!'.format(nome))
print('Prazer {:<20}!'.format(nome))#alinhado a esquerda
print('Prazer {:>20}!'.format(nome))#alinhado a direita
print('Prazer {:^20}!'.format(nome))# centralizado
print('Prazer {:=^20}!'.format(nome))#cria = e centraliza a palavra no meio

num1 = int(input('Entre com um numero: '))
num2 = int(input('Entre com um numero: '))

soma = num1 + num2
div  = num1 / num2
prod = num1 * num2
divInt = num1 // num2
exp = num1 ** num2

                                        # :.3f informa que deve ter apenas 3 casas
print('A soma é {}, divisão {}, produto {:.3f} '.format(soma, div, prod), end=' ') # end ='' não quebra a linha no print
print('A divisão inteira {}, potência {} '.format(divInt, exp))