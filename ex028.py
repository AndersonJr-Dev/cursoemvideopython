from random import randint
from time import sleep
computador=randint(0,5) #faz o computador pensar em um numero
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador=int(input('Em que numero eu pensei? '))#jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no {} e não no {}!'.format(computador,jogador))



