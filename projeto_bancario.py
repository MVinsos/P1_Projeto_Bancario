import textwrap

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


def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")

    else:
        print("Valor inválido, por favor digite um valor válido")

    return saldo, extrato


def saque(*, valor, saldo, limite, limite_saques, numero_saques, extrato):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente.")

    elif excedeu_limite:
        print("Limite do valor de saque excedido.")

    elif excedeu_saque:
        print("Limite diario de saques excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso.")

    return saldo, extrato, numero_saques
    

def exibir_extrato(saldo, /, *, extrato):
    print("\n====================EXTRATO==================")
    print("Nenhuma movimentação realizada durante o periodo solicitado." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("===============================================")


def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado, por favor verifique a lista de contas!")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço completo (logradouro, nro - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None 


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado ou número inválido.")


def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = "0001"
    
    while True:

        opcao = menu()

        if opcao == "d":
            while True:
                valor = input("Informe o valor do depósito: ")
                if not valor.isdigit():
                    print("Valor inválido. Por favor, digite um valor numérico.")
                    continue
                valor = float(valor)
                saldo, extrato = deposito(saldo, valor, extrato)
                break 


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                valor=valor,
                saldo=saldo,
                limite=limite,
                limite_saques=limite_saques,
                numero_saques=numero_saques,
                extrato=extrato
            )


        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
    

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
            print("Operação invalida, por favor selecione uma operação valida.")
        


main()