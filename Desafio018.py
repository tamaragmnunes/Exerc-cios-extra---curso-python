# Faça um programa que leia um ângulo qualquer e leia o seu seno, cosseno e tangente
from math import sin, cos, tan
x = int(input('Digite o ângulo: '))
print ('Para o ângulo {}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente {:.2f}'.format (x,sin(x),cos(x),tan(x)))

