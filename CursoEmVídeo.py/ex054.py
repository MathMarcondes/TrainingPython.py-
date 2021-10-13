# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
x = 0 
n = 0
for c in range(1, 8):
    nasc = int(input('Digite a data do seu nascimento: '))
    idade = atual - nasc
    if atual >= 18:
        x+=1
    else:
        n+=1
        
print(f'{x} Pessoas atingiram a maioridade')
print(f'{n} Pessoas ainda não atingiram a maioridade')
