'''''


Faça um algoritmo que calcule e apresente o valor do volume de uma lata de 
óleo, utilizando a fórmula VOLUME = 3,14159 * RAIO2
 * ALTURA.
'''
raio = int(input('Qual é o raio da lata: '))
altura = float(input('Qual é a altura da lata: '))

volume = 3.14159 * raio**2 * altura

print(f'O volume da lata é de: {volume}')