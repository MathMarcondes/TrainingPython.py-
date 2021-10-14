# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Quantos termos você quer usar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}')
cont = 3
while cont<=n:
    t3 = t1 + t2
    print(f'{t3}')
    t1 = t2
    t2 = t3
    cont +=1