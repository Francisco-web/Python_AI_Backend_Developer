

#while é usado para repetir um bloco de código varias vezes, quando não sabemos o número exato de vezes que o nosso bloco deve ser executado
#else usamos com while caso não cumpir com  condição verdadeira
#break quebrar ou interromper o laço durante a execução

opcao = 1
'''
while opcao != 0:
    opcao = int(input('[1]Tirar dinheiro \n[2]Extrato \n[0]Sair \n'))

    if opcao == 1:
        print('A tirar dinheiro...\n')
    elif opcao == 2:
        print('A Mostrar Extrato \n')
else:
    print('Onrigado pela preferência. Volte sempre!')

while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        
        break  
    print(numero, end=" ")

'''''
#mostrar numero impares
#continue pula a execução para proxima.

for numero in range(100):
    if numero % 1:
        continue
    print(numero, end=" ")