


#pode armazena qualquer tipo de valores. O armazenamento pode ser seuencial
#podemos criar listas utilizando o construtor (list), a outra é colocar colchetes [] e  colocar valores dentro deles

fruit = ["Apple","orange","Mango"]

print(f"Fruits: {fruit}")

#é possivel declarar uma lista vazia
fruits = []
##print(fruits)

letters = list("python")
#print(f"Letters : {letters}")

#constructor (list)
numbers = list(range(10))
#print(f"Number: {numbers}")
#Podemos criar listas com diferentes valores
car = ["Ferrari","F8",23456,2024,"Luanda", True]
#print(f"cars: {car}")

####Podemos acessar os dados de uma lista de algumas formas:
    #1.Acesso direto: utilizando índices ou posicões que começam apartir de zero
        #É Possivel que os indices da lista sejam vazios

fruit[0]
fruit[1]
#print(f"fruits: {fruit[0]},{fruit[1]}")

    #2.Listas aninhadas: usada em matriz bidimencional. Lista podem armazenar todos os tipos de objecto, existem perigo. Aqui eu posso acessar informando os indices, esta lista ou matriz é formada por linhas e colunas. 
    #usamos matriz para inserir valores na lista, mais comum é a bidimencional
    
matriz = [
        [1,2,3,4],
         ["Ave",3,5,9],
         ['10',13,0,20]
]
matriz[0] #significa que quero apenas uma linha
matriz[0][0] # [0]linha [0]coluna
matriz[0][-1] #Nã há problema em considerar número negativo
matriz[-1][-1]
print(matriz)

#3. Fatiamneto: extrai um conjunto de valores de uma sequência. informa também quanta posições o cursor deve "pulars    
lista = ["P","y,""t","h","o"]

lista[12:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[4:2]
lista[12:]

