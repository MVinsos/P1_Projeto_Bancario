import textwrap
from abc import ABC, abstractmethod
from datetime import date

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta._saldo += self.valor
            conta._historico.adicionar_transacao(f"Depósito: R$ {self.valor:.2f}")
            return True
        else:
            print("Valor de depósito inválido.")
            return False

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0 and self.valor <= conta._saldo:
            conta._saldo -= self.valor
            conta._historico.adicionar_transacao(f"Saque: R$ {self.valor:.2f}")
            return True
        else:
            print("Valor de saque inválido ou saldo insuficiente.")
            return False

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero, agencia):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero, agencia):
        return cls(cliente, numero, agencia)
    
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        transacao = Saque(valor)
        return transacao.registrar(self)
    
    def depositar(self, valor):
        transacao = Deposito(valor)
        return transacao.registrar(self)

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite=500.0, limite_saques=3):
        super().__init__(cliente, numero, agencia)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor):
        if self._saques_realizados >= self._limite_saques:
            print("Limite de saques diários excedido.")
            return False
        if valor > self._limite:
            print("Valor de saque excede o limite.")
            return False
        if super().sacar(valor):
            self._saques_realizados += 1
            return True
        return False

class Cliente(ABC):
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        if conta in self._contas:
            return transacao.registrar(conta)
        else:
            print("Conta não pertence ao cliente.")
            return False

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

def menu():
    menu = """\n
===========BEM-VINDO AO MENU============
            [d] Deposito
            [s] Saque
            [e] Extrato
            [u] Cadastrar Novo Usuário
            [c] Criar Nova Conta
            [l] Lista de Contas
            [q] Sair

=> """
    return input(textwrap.dedent(menu))

def exibir_extrato(conta):
    print("\n====================EXTRATO==================")
    if not conta._historico.transacoes:
        print("Nenhuma movimentação realizada durante o período solicitado.")
    else:
        for transacao in conta._historico.transacoes:
            print(transacao)
    print(f"\nSaldo: R$ {conta.saldo():.2f}")
    print("===============================================")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado, por favor verifique a lista de contas!")
        return
    
    nome = input("Nome completo: ")
    while True:
        data_nascimento_str = input("Data de nascimento (dd-mm-aaaa): ")
        try:
            dia, mes, ano = map(int, data_nascimento_str.split('-'))
            data_nascimento = date(ano, mes, dia)
            break
        except ValueError:
            print("Data de nascimento inválida. Por favor, tente novamente. (Não se esqueça de adicionar '-' entre dia, mes e ano)")
    
    endereco = input("Endereço completo (logradouro, nro - bairro - cidade/estado): ")
    
    usuario = PessoaFisica(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)

    print("Usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if isinstance(usuario, PessoaFisica) and usuario._cpf == cpf:
            return usuario
    return None 

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        conta = ContaCorrente(usuario, numero_conta, agencia)
        usuario.adicionar_conta(conta)
        print("\nConta criada com sucesso!")
        return conta
    
    print("Usuário não encontrado ou número inválido.")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta._agencia}
            C/C:\t\t{conta._numero}
            Titular:\t{conta._cliente._nome}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def selecionar_conta(usuario):
    if len(usuario._contas) == 1:
        return usuario._contas[0]
    print("Contas disponíveis:")
    for conta in usuario._contas:
        print(f"Conta: {conta._numero}, Agência: {conta._agencia}")
    
    while True:
        numero_conta = int(input("Informe o número da conta que deseja acessar: "))
        conta = next((c for c in usuario._contas if c._numero == numero_conta), None)
        if conta:
            return conta
        else:
            print("Conta não encontrada. Por favor, tente novamente.")

def main():
    usuarios = []
    contas = []
    agencia = "0001"
    
    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe seu CPF (somente números): ")
            usuario = filtrar_usuarios(cpf, usuarios)
            if usuario:
                conta = selecionar_conta(usuario)
                while True:
                        try:
                            valor = float(input("Informe o valor do depósito: "))
                            if valor <= 0:
                                print("Valor de depósito inválido. Deve ser maior que 0.")
                                continue
                            break
                        except ValueError:
                            print("Valor inválido. Por favor, insira um número.")
                    
                if conta.depositar(valor):
                        print("Depósito realizado com sucesso!")
                else:
                    print("Conta não encontrada.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "s":
            cpf = input("Informe seu CPF (somente números): ")
            usuario = filtrar_usuarios(cpf, usuarios)
            if usuario:
                conta = selecionar_conta(usuario)
                while True:
                    try:
                        valor = float(input("Informe o valor do saque: "))
                        if valor <= 0:
                            print("Valor de saque inválido. Deve ser maior que 0.")
                            continue
                        break
                    except ValueError:
                        print("Valor inválido. Por favor, insira um número.")
                
                if conta.sacar(valor):
                    print("Saque realizado com sucesso!")
            else:
                print("Usuário não encontrado.")

        elif opcao == "e":
            cpf = input("Informe seu CPF (somente números): ")
            usuario = filtrar_usuarios(cpf, usuarios)
            if usuario:
                conta = selecionar_conta(usuario)
                exibir_extrato(conta)
            else:
                print("Usuário não encontrado.")

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "l":
            lista_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione uma operação válida.")

main()
