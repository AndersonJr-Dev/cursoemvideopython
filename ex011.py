n1largura = float(input('Digite a largura da parede: '))
n2altura = float(input('Digite a altura da parede? '))
soma = n1largura * n2altura
print('A sua parede tem a dimensão de {}m x {}m e sua área total é de {}m².'.format(n1largura, n2altura, soma))
print('A quantidade necessaria de tinta para pintar a parede é de {:.1f}l.'.format(soma / 2))
