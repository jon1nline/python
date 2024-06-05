def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Deposito realizado com sucesso. saldo da conta atual: R${saldo:.2f}")
    else:
        print("Operação falhou! o valor digitado é inválido.")
            
    return(saldo, extrato)        

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite de R$500,00.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários (3) excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print('Você ainda pode sacar ',(limite_saques - numero_saques),'vezes')

    else:
        print("Operação falhou! O valor informado é inválido.")

    return(saldo, extrato)
    
def exibir_extrato(saldo, /, *, extrato):
    if not extrato:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    else:
        print("\n================ EXTRATO ================")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe uma conta cadastrada com esse CPF")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço completo, incluindo numero, bairro, cidade e estado: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Sua conta foi aberta com sucesso.")
        print('agencia: ', agencia,'\n conta: ',numero_conta)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("usuário não encontrado. crie um para poder abrir sua conta.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        ==================================
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        ===================================
        """
        print((linha))


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[a] abrir conta
[l] Listar contas
[n] Novo Usuário
[q] Sair

=> """

LIMITE_SAQUES = 3
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []



while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que deseja depositar: "))
        saldo, extrato = depositar(saldo, valor, extrato)
      
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))
        saldo, extrato = saque(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            limite_saques = LIMITE_SAQUES,
            )
        
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
        
    elif opcao == "a":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        if conta:
            contas.append(conta)
           
    elif opcao == "n":
        criar_usuario(usuarios)
        
    elif opcao == "l":
        listar_contas(contas)  
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor escolha uma das opções abaixo.")
