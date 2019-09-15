# Faça um  programa que leia o comprimento  do cateto oposto e do cateto adjacente  de um triângulo
# retângulo, calcule e mostre a hipotenusa

'''
a = float(input('Cateto oposto: '))
b = float(input('Cateto adjacente: '))
x = (a**2 + b**2)**(1/2)
print ('A hipotenusa é: {:.2f}'.format (x))
'''
from math import hypot
a = float(input('Cateto oposto: '))
b = float(input('Cateto adjacente: '))
print ('A hipotenusa é:', hypot(a, b))

