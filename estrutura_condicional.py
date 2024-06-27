#if simples
import sys

"""
saldo = 5000.0
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("Realizando Saque!")
else:
    print("saldo Insuficiente!")

#varios if aninhado
opcao = int(input("Informe uma opcao:[1]Sacar \n[2] Extrato: "))
if opcao == 1:
    valor= float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o Extradto...")
else: sys.exit("Opcao Inválida") 

#Exemplo, calcular idade

MAIOR_IDADE = 18

idade = int(input("insira a sua idade: "))
if idade >=MAIOR_IDADE:
    print("Maior de idade pode tirar  a carta de condução")
else: print("Ainda não pode tirar a carta de condução.")

#if ternário permite escrever a condição em uma unica linha
saldo = 1000
saque = 2000
status = "sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
"""
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2)//2
resultado = "Aprovado" if media >= 10 else "Repovado"
print(f"Nota {media}, Aluno {resultado}") 
