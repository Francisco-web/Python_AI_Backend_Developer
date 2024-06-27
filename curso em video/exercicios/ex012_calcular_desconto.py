preco = float(input('Preço do produto: '))
desconto = preco * (5/100) 

novoPreco = (preco - desconto)
print(f'Valor de desconto: {desconto}\n Novo preço: {novoPreco}')