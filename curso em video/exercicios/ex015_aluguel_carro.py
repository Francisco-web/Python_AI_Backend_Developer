dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))

pago = (dia*60) + (km*0.15)
print('A conta a pagar é {:.2f}kz'.format(pago))