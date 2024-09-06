def formatar(valor):
    num_valor = str(valor)
    if "." not in num_valor:
        num_valor = num_valor + '.00'
    return num_valor

menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

lextrato = []


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = input()

        if float(valor_deposito) > 0:
            saldo = saldo + float(valor_deposito)
            lextrato.append ("R$ " + formatar(str(valor_deposito)) + " C ")
        else:
            print("Valor inválido !")    

    elif opcao == "s":
        print("Saque")
        valor_saque = input()

        if float(valor_saque) > 0:
            if numero_saques < 3:
                if float(valor_saque) <= 500:
                        if float(valor_saque) <= saldo:
                            numero_saques = numero_saques +1
                            saldo = saldo - float(valor_saque)        
                            lextrato.append ("R$ " + formatar(str(valor_saque)) + " D ")
                        else:
                            print("Saldo insuficiente !")    
                else:
                    print("Limite de saque excedido !")    
            else:
                print("Número de saques excedido !")     
        else:
            print("Valor inválido !")                      

    elif opcao == "e":
        print("=====================")
        print("Extrato:")
        print("")
        for x in range(len(lextrato)):
            print (lextrato[x])
        print("")        
        print(f"Saldo = R$ {saldo:.2f}")
        print("=====================")

    elif opcao == "q":
        break                       

    else:
        print("Opção inválida !. Selecionar novamente.")