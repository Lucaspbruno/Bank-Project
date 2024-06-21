

def menu ():
   lista = """

   [d]   Depositar
   [s]   Sacar
   [e]   Extrato 
   [nu]  Novo Usuario
   [c]   Criar Conta Corrente
   [lc]  lista de conta corrente
   [ls]  lista de usuarios
   [q]   Sair

   => """

   return input(lista)

def deposito (valor,saldo,extrato,/):

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print("Depósito Realizado com Sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

        return saldo, extrato

def saque (*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

            print("Operação Realizada com Sucesso!")

    else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato        

def extrato_conta (saldo, /, *,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return saldo, extrato

def novo_usuario (contas):
     cpf = input("Informe o seu CPF (somente número): ")
     usuario = verificar_usuario(cpf, contas)

     if usuario:
          print("Cpf invalido, por favor insira novamente.")
          return main

     nome = input("Informe o nome completo: ")
     data_nascimento = input("Data de nascimento: ")
     endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

     contas.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

     print("========= Usuário criado com sucesso! ========")

def verificar_usuario(cpf, contas):
    usuarios_filtrados = [usuario for usuario in contas if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
        print("\n Usuário não encontrado, Por favor tente novamente")
        return main




def main():
    usuario = []
    contas = []


    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()
        
        
        if opcao == "d":
            valor = float(input("Digite o Valor que Deseja Depositar:"))
            saldo, extrato = deposito (valor, saldo, extrato)

    
        elif opcao == "s":
            valor = float(input("Digite o Valor que Deseja Sacar:"))
            saldo, extrato = saque(
                  saldo = saldo,
                  valor = valor,
                  extrato = extrato,
                  limite = limite,
                  numero_saques = numero_saques,
                  limite_saques = LIMITE_SAQUES,)
        

        elif opcao == "e":
            extrato_conta(saldo,extrato = extrato)
            
        
        elif opcao == "nu":
            novo_usuario(usuario)

        elif opcao == "c":
             numero_conta = len(contas) + 1
             contas = criar_conta_corrente(AGENCIA, numero_conta, usuario)

        elif opcao == "lc":
             print(contas)     

        elif opcao == "ls":
            print(usuario,"Agencia:",AGENCIA)         

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()