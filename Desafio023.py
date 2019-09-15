# Faça um programa que leia o número de 0 a 9999 e mostre cada  um dos digitos separados

num = int(input('Digite um número: '))
n = str(num)

print('Analisando o número {}'.format(num))
print('Unidade:{}'.format(n[-1]))
print('Dezena:{}'.format(n[-2]))
print('Centena:{}'.format(n[-3]))
print('Milhar:{}'.format(n[-4]))
print('Fim do programa!')
