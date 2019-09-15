# Faça um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Digite o seu salário: '))
novoSalario = salario*(15/100)
print ('O seu novo salário com reajuste de 15% é {}'.format(salario+novoSalario))