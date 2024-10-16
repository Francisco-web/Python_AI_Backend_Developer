''''
car = [["vemelho,BNW"],
["vemelho,BNW"]]

for car in car :
    print(car)

#função enumerate: deve conhecer o indice no  F. par isso usamos a função (enumerate)
for indice, cars in enumerate(car):
    print(f"{indice}: {cars}")

#Comprensão de lista: permite criar uma lista com base em valores já existentes
#append adiciona novos valores na lista
numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

#filtro versão 1
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
'''
#modificando valores verão 1
numeros = [1,30,21,2,9,65,34]
quadrado = []
for numero in numeros :
    quadrado.append(numero **2)
print(quadrado)
