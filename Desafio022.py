'''
Crie um programa em python que leia o nome completo  de uma pessoa e mostre
1. O nome com todas as letras maiúsculas
2. O nome com todas minúsculas
3. Quantas letras ao todo sem considerar espaços
4. Quantas letras tem o primeiro nome
'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('O seu nom em maiúsculas é {}'.format(nome.upper()))
print('O seu nome em minúsculas é {}'.format(nome.lower()))
print('O seu nome completo tem {} letras.'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
