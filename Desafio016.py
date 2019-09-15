# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
n = float(input('Digite um número: '))
print ('O número {} tema parte inteira {}'.format(n, trunc(n)))

# trunc é uma função da biblioteca math que corta a parte inteira de um número decimal