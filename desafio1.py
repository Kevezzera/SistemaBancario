menu = """
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numer_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou")

    elif opcao == "s":
        print("saque")
        valor = float(input("Informe o valor do deposito: "))

        excedeu_saldo = valor > saldo

        excede_limite = valor > limite

        excede_saque = numer_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou. Saldo insuficiente.")

        elif excede_limite:
            print("Valor excedido.")

        elif excede_saque:
            print("Numero de saques excdidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numer_saques += 1 

        else:
            print("Valor invlido!")

    elif opcao == "e":
        print("Extrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")

    elif opcao == "q":
        break
    
    else:
        print("Operação invalida!!")