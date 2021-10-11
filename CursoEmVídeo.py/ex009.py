# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

tab = int(input('Digite o valor que deseja saber a tabuada: '))
c = 0
s = 0
while c <= 10:
    s = tab * c
    print(f'{c}x{tab}={s}')
    c+=1
print('fim')
    