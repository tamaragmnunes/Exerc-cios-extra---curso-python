# Digite o seu nome completo e mostre o seu primeiro nome e o último

nome = str(input('Digite o seu nome completo: ')).split()
print('O seu primeiro nome é {}.'.format(nome[0]))
print('O seu último nome é {}.'.format(nome[-1]))
print('Fim do programa!!! :)')
