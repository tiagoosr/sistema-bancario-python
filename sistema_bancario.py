from datetime import datetime
import textwrap

def menu(): 
    menu = """
    ================ MENU ================

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [cc]\tCriar conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [lm]\tListar compras
    [q]\tSair

    Escolha uma opção: 
    => """
    return input(textwrap.dedent(menu))



def registrar_transacao(tipo, valor, extrato):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato += f"{agora} - {tipo}: R$ {valor:.2f}\n"

    return extrato


def depositar(saldo,valor, extrato, qtd_transacoes, transacoes_diarias, /):

    if qtd_transacoes >= transacoes_diarias:
        print("Limite de transações diárias atingido.")
        return
    
    if valor > 0:
        saldo += valor
        qtd_transacoes += 1
        extrato = registrar_transacao("Depósito", valor, extrato)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O depósito deve ser positivo.")

    return saldo, extrato



def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, qtd_transacoes, transacoes_diarias):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if qtd_transacoes >= transacoes_diarias:
        print("Você excedeu o número de transações diárias permitidas.")
        return
    
    if excedeu_saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif excedeu_limite:
        print("Limite por saque é de R$ 500.00")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        qtd_transacoes += 1
        extrato = registrar_transacao("Saque", valor, extrato)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. O saque deve ser positivo.")
    
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n" + " EXTRATO ".center(40, "="))

    if not extrato:
        print("Nenhuma movimentação realizada..")
    else:
        print(extrato, end="") 

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=".center(40, "="))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        print("Já existe usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf, 
        "endereco": endereco
    })

    print("=== Usuário criado com sucesso! ===")
    

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

def listar_compras(compras):
    print("\n" + " COMPRAS ".center(40, "="))
    if not compras:
        print("Nenhuma compra realizada.")
    else:
        for compra in compras:
            print(compra)
    print("=" * 40)
   

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    compras = []
    transacoes_diarias = 10
    qtd_transacoes = 0

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor para depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato, qtd_transacoes, transacoes_diarias)

        elif opcao == "s":
            valor = float(input("Informe o valor para saque: "))
            saldo, extrato = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite,
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES,
                qtd_transacoes=qtd_transacoes, 
                transacoes_diarias=transacoes_diarias
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "lm":
            listar_compras(compras)

        elif opcao == "q":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()