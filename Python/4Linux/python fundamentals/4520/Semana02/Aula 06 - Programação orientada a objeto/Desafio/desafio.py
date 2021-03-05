#!/usr/bin/python3


# Desafio – Criando objetos

# Neste desafio iremos treinar o conhecimento que adquirimos na Aula de Orientação a objetos , Faça uma abstração de uma conta de corrente que tenha no mínimo 3 métodos (sacar, depositar, transferir), instancie a classe poupança herdando de conta corrente, porém deve realizar um método com polimorfismo e incrementar o método render juros.

# Para concluir este desafio:

# Deve utilizar os conceitos de orientação a objetos, utilizar método construtor atribuir características e comportamentos.

def linha(tipo_linha):
    print(20 * tipo_linha)

class Conta():
    
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        """
        depositando
        """
        self.saldo += valor

    def transferir(self, valor, conta):
        """
        transferindo
        """
        self.sacar(valor)
        conta.depositar(valor)


class Poupanca(Conta):
    def __init__(self, titular, numero_conta, saldo):
        super().__init__(titular, numero_conta, saldo)
        self.juros = 0.005
    def render_juros(self):
        self.saldo += self.saldo * self.juros

c1 = Conta('Danel', 12345, 1500)

c2 = Conta('Wesley', 388984, 1500)

c3 = Poupanca('Jair', 9843479, 1500)

lin = str(input('entre com o tipo de linha\n'))
print(c1.saldo, c1.titular, sep='\n')
linha(lin)

print(c2.saldo,c2.titular, sep='\n')
linha(lin)

print(c3.saldo, c3.titular, c3.render_juros(), sep='\n')
linha(lin)

c1.transferir(500, c2)

print(c1.saldo, c2.saldo, sep='\n')
linha(lin)
print(c3.saldo, c3.titular, sep='\n')



