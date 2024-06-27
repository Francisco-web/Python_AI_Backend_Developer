salario = float(input('Digite o seu salário: '))
bonus = salario * (15/100)
novo_salario = bonus + salario
print('Bonus: {:.2f}\nNovo salário: {:.2f}'.format(bonus,novo_salario))