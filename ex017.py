import math
cateto=float(input('Digite o comprimento do cateto oposto: '))
adj=float(input('Digite o comprimento do cateto adjacente: '))
hip=math.hypot(cateto,adj)
print('A hipotenusa vai medir {:.2f}'.format(hip))




