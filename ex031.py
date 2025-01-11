km=float(input('Digite a distancia da sua viagem: '))
if km <= 200:
    print('O valor da passagem será de R${:.2f}'.format(km*0.50))
else:
    print('O valor da passagem será de R${:.2f}'.format(km*0.45))

