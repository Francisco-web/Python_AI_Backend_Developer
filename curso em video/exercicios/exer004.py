


#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
#isspace() metodo padrão

a = input('Digite algo: ')
print('O tipo primmitivo desse valor é ', type(a)) 
print('Só tem espaço? ',a.isspace())
print('É um número? ',a.isnumeric())
print('È alfabetico? ',a.isalpha())
print('É alfaNumerico? ',a.isalnum())
print('Está em Maiuscula? ',a.isupper())
print('Está minuscula?',a.islower())
print('Está CApitalizada(a primeira letra é maiuscula)?',a.istitle())
