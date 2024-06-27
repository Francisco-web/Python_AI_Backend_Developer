

#For percorre um objecto iterável. Usamos quando sabemos o número de vez que deve ser repetido
''''
texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
    
print()
'''
#for else / Laços
#range - intervalo do limite de contagem
# o range tem 3 argumento (start, stop, step)
''''
inicio = int(input('Inicio: '))
passo = int(input('Passo: '))
fim = int(input('Fim: '))
for c in range(inicio,fim +1,+ passo):
    print(c)
print('FIM!')
'''
#mostrar numero impares
#continue pula a execução para proxima.
#break quebrar ou interromper o laço durante a execução

for numero in range(100):
    if numero % 1:
        continue
    print(numero, end=" ")