dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
valor = (dias * 60) + (km * 0.15)
print('O total a pagar pelo aluguel do carro é de R${:.2f}'.format(valor))
