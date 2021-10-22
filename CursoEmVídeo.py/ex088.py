# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint 
lista = list()
print('=-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0

num = randint(1, 60)
cont = 0
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont+=1
    if cont >= 6:
        break
print(f'Os números sorteados foram {lista}')

