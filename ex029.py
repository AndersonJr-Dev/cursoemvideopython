km=float(input('A que velocidade o carro está? KM'))
if km >80:
    print('\033[4;30;41mMULTADO! Você excedeu o limite permitido que é de 80 KM/H\033[m')
    print('O valor da multa será de {} reais.'.format((km-80)*7))
else:
    print('Parabéns você não foi multado')
