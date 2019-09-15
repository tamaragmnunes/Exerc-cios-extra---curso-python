# O mesmo professor do desafio anterior quer sortear a ordem  de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
PrimeiroAluno = str(input('Digite o primeiro nome: '))
SegundoAluno = str(input('Digite o segundo nome: '))
TerceiroAluno = str(input('Digite o terceiro nome: '))
QuartoAluno = str(input('Digite o nome do quarto aluno: '))
lista = [PrimeiroAluno,SegundoAluno,TerceiroAluno,QuartoAluno]
shuffle(lista)
print ('A ordem de apresentação será {}'.format(lista))