menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Opçao: """



saldo = 0
saque = 0
quantidade_permitida_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        deposito_conta = float(input("Digite o Valor que deseja depositar:"))

        if deposito_conta > 0:        
            saldo += deposito_conta
            extrato += f"Depósito: R$ {deposito_conta:.2f}\n"
            print(extrato)
             
            print(f"O saldo da conta é R$ {saldo:.2f}")
            
        else:
            print("Operaçao falhou tente novamente!")    
            


    elif opcao == "2":
        

        saque = float(input("Digite quanto deseja sacar:"))

        if saque <= quantidade_permitida_por_saque and saque > 0:
             if numero_saques <= LIMITE_SAQUES:
                 numero_saques += 1
                 saldo -= saque
                 extrato += f"Saque: R$ {saque:.2f}\n"
                 print(extrato)
                 print(f"O saldo da conta é R$ {saldo:.2f}")
                 

             else:
                print("A Quantidade de saques excedeu o permitido")  

        else:
            print("A operação falhou, tente novamente!")               
        
        

    elif opcao == "3":
        print(extrato)
        print(f"Saldo da conta : R$ {saldo:.2f}")
        print("Obrigado por Usar nossos serviços!")

    elif opcao == "4":
        print("Obrigado Por Usar Nossos Serviços!")
        break

    else:
        print("Operação Invalida, Por Favor Digite Novamente:")            



  





