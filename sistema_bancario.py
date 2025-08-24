menu = """
===== MENU =====

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha uma opção: 
"""

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O depósito deve ser positivo.")

def sacar(valor):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif excedeu_limite:
        print("Limite por saque é de R$ 500.00")
    elif excedeu_saques:
        print("Você já atingiu o limite diário de saques (3).")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O saque deve ser positivo.")


def exibir_extrato():
    print("\n" + " EXTRATO ".center(40, "="))
    print("Nenhuma movimentação realizada.." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=".center(40, "="))


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: "))
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))
        sacar(valor)

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")