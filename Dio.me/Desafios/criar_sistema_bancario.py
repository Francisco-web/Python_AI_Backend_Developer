
#Operaçõoes: deposito, saque, extrato
#deposito: perguntar o valor a depoitar, deve depositar valores positivo, 
#os dados do deposito deve estar armazenado para consulta ou extrato
#Saque: deve permitir realizar 3 saques diarios com limite maximo de R$ 500,00 por saque. exibir mensagem que não sera possivel sacar o diheiro por falta de saldo. todos os saques devem ser armazenados e consultado em uma variavel e exibidos na operação de esxtrato
#extrato: listar depoitos e sques e saldo actual exibir no formato R$1500.00 

menu = """
        Seja Bem vindo ao Banco Dio.Me
        1- Depositar
        2- Sacar
        3- Extrato
        0- Sair
       """
limite = 500
saldo = 0
numero_saque = 0
extrato = 0
operacao = 1
LIMITE_SAQUES = 3
valor_depositado, valor_saque, saldo = 0,0,0

while operacao !=0:
    operacao = int(input(menu))
    if operacao == 1:
        
        print('1.Depositar dinheiro')
        valor_depositado = float(input('Quanto vai depositar? '))
        if valor_depositado <= 0 :
            print('O valor Inserido é inválido!')
        else:
            print(f'R${valor_depositado}, Deposito feito com sucesso!')
            saldo += valor_depositado
            extrato += valor_depositado

    elif operacao == 2:
        print('2.Sacar Dinheiro')
        if numero_saque == LIMITE_SAQUES:
            print('Você atingiu o limite de saque! Não será possível sacar o dinheiro.')
        else:
            valor_saque = float(input('Qual é o valor do saque? '))
           
            opcao = input(f'\nValor a sacar: {valor_saque:.2f}. Confirmar?\n[s]-Sim\n[n]-Não\n')
            if opcao == 's' or 'S':
                if valor_saque > 0:
                    if valor_saque > saldo:
                        print('Não será possivel sacar o diheiro por falta de saldo na Conta!')
                    elif valor_saque > limite:
                        print('O limite maximo é de R$ 500,00 por saque. Não será possível sacar o diheiro por falta de saldo.')
                    else:
                        print('Saque feito com sucesso!')
                        saldo -= valor_saque 
                        extrato += valor_saque
                        numero_saque += 1  
                else:
                    print('O valor Inserido é inválido!')

            else:
                print('Operação cancelado!')  

    elif operacao == 3:
        print(f'''
                Extrato Deposito
                    R${valor_depositado:.2f}

                Extrato Saque
                    R${extrato:.2f}

                Extrato Saldo Actual
                    R${saldo:.2f}

            ''')
else: 
    print('Você Saiu do Sistema Bancário!')
