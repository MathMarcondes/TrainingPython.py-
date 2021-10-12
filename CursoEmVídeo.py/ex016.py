# Crie um programa que leia um número Real qualquer pelo teclado e 
# mostre na tela a sua porção Inteira.
from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor real arredondado para inteiro ficaria: {n} e sua porção inteira ficaria {(trunc(n))}')