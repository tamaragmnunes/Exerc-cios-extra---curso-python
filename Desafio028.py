'''
Escreva um programa que faça o computador pensar
em um número inteiro  entre 0 e 5  e peça para o usuário
tentar decobrir qual foi o número escolhido pelo computador.

O programa deverá  se o usuário venceu ou perdeu.
'''
from random import randint
num = int(input('Digite um número entre 0 e 5: '))
r = randint(0,1)
if num == r:
    print('Você acertou! PARABÉNS KKKKK')
else :
    print('Você errou! O número escolhido foi {}'.format(r))
print('FIM DO JOGO!')