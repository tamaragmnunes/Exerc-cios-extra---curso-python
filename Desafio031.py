'''
Desenvolva um programa que pergunte  a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200km e R$0,45 para viagens mais longas.
'''
nome = str(input('Qual é o seu nome?' ))
distancia = int(input('Qual é a distância da viagem? '))
if distancia <=200:
    print('A sua viagem custa R${} reais.'.format(distancia*0.5))
else:
    print('A sua viagem custa R${} reais.'.format(distancia*0.45))
print('Olá, {}! Tenha uma boa viagem!!!'.format(nome))