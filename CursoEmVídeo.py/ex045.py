

from random import randint 
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('''Suas opções
[ 1 ] Pedra
[ 2 ] Tesoura
[ 3 ] Papel''')
jogador = int(input('Qual a sua jogada? '))
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador perdeu')
    elif jogador == 2:
        print('Jogador Ganhou')
elif jogador == 0:
    if computador == 0:
        print('Empate')
    elif computador == 1:
        print('Pc venceu')
    elif computador == 2:
        print('Pc perdeu')