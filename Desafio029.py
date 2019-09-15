'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 para cada km acima do limite.
'''
velocidade = int(input('Qual a velocidade do carro? '))
custo = 7*(velocidade-80)
if velocidade >= 80:
    print('Você excedeu o limite de velocidade. Você deve pagar R${},00 reais.'.format(custo))
else:
    print('Parabéns, você está na velocidade permitida por lei.')
