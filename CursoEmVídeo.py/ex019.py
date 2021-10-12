# Um professor quer sortear um dos seus quatro alunos 
# para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo na tela o nome do 
# escolhido.

import random
for c in range(1, 6):
    n = str(input('Aluno: '))
lista = [n]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))