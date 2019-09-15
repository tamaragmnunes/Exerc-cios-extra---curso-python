'''
Escreva um programa  que pergunte  o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a  R$1250,00, calcule um aumento de 10%
Para os inferiores ou igual, o aumento é de 15%.
'''
nome = str(input('Qual é o seu nome? '))
salario = float(input('Didite o seu salário: '))
aumento10 = (10/100*salario)+salario
aumento15 = (15/100*salario)+salario
if salario >= 1250:
    print('O seu salário de {} com aumento de 10% fica {} reais.'.format(salario, aumento10))
else:
    print('O seu salário de {} com aumento de 15% fica {} reais.'.format(salario, aumento15))
print('Faça bom proveito!!!')