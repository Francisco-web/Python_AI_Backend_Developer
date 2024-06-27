

#identação maonter o codigo fonte mais legivel e manutenivel. Determina onde começa e termina um bloco de codigo
#utilizar espaco, apenas 4 espaços para identar

#exemplo de identação

def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado")

    print("Obrigado por esclher nosso banco")#esse codigo não esta dentro do if
sacar(100)