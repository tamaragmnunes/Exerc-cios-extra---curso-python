# Faça um programa que leia  um ano qualquer e mostre se ele é bissexto

ano = int(input('Digite um ano qualquer: '))
bis = (ano/4)
if bis == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))