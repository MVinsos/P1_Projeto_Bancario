menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso")


        else:
            print("Operação falhou. O valor informado é invalido.")


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

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



    elif opcao == "e":
        print("\n====================EXTRATO==================")
        print("Não movimentação realizada durante o periodo solicitado." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("===============================================")


    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione uma operação valida.")