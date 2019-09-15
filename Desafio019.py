# Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo os nomes deles
# e escrevendo o nome escolhido
import random
PrimeiroAluno = str(input('Digite o primeiro nome: '))
SegundoAluno = str(input('Digite o segundo nome: '))
TerceiroAluno = str(input('Digite o terceiro nome: '))
QuartoAluno = str(input('Digite o quarto aluno: '))
lista = [PrimeiroAluno,SegundoAluno,TerceiroAluno,QuartoAluno]
escolhido = random.choice(lista)
print ('O aluno escolhido foi {}'.format(escolhido))
