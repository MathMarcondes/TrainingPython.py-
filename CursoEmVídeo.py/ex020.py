# O mesmo professor do desafio 19 quer sortear a ordem de
#  apresentação de trabalhos dos alunos. Faça um programa
#  que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
for c in range(0, 3):
    n = str(input('Aluno: '))

lista = [n]
random.shuffle(lista    )
print('A ordem de apresentação será: ')
print(lista)

