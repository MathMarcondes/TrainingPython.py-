# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça 
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá 
# escrever na tela se o usuário venceu ou perdeu.
from random import randint

pc = randint(0, 5)
print('='*20)
player = int(input('Em qual número estou pensando? '))
print('='*20)
if player == pc:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! O número sorteado foi {} e você selecionou {}'.format(pc, player))
