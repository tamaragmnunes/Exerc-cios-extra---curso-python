'''
Crie um programa que leia a altura e largura de uma parede  em metros, calcule sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 m2
'''

altura = float(input('Qual é a altura da parede? '))
largura = float(input('Qual é a largura da parede? '))
area = altura*largura
tinta = area/2
print('A sua parede tem  a de dimensão de  {} x {} e sua área é de {}.'. format(altura, largura, area))
print ('A quantidade de tinta necessária para pintar a sua parede é: {} litros de tinta.'.format(tinta))