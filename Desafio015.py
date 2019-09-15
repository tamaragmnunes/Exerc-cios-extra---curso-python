'''
Escreva um programa que pergunte a quantidade de Km percorridos por
um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

km = int(input('Quantos km o carro percorreu? '))
dias = int(input('Quantos dias ficou alugado? '))
custo1 = dias*60
custo2 = km*0.15
print ('O carro ficou alugado por {} dias e percorreu {} km. \n Portanto o valor a ser pago será: R$ {}.'.format(dias, km, custo1+custo2))
