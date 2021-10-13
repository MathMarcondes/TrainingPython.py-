# Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Digite um número para calcular seu factorial: '))
c = n
while c>0:
    print('{c} x')
    c-=1 
print(f'O fatorial de {n} é {c}')
