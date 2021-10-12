# Faça um programa que leia um ângulo qualquer e mostre na 
# tela o valor do seno, cosseno e tangente desse ângulo.

import math 
ângulo = float(input('Digite o valor do ângulo que deseja saber o seno: '))
seno = math.sin(math.radians(ângulo))
print('O âgnulo {:.2f} tem o seno {:.2f}'.format(ângulo, seno))
coss = math.cos(math.radians(ângulo))
print('O âgulo de {:.2f} tem o cosseno de {:.2f}'.format(ângulo, coss))
tg = math.tan(math.radians(ângulo))
print('O ângulo de {:.2f} tem a tangente de {:.2f}'.format(ângulo, tg))
