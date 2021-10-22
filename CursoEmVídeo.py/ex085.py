# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor %2==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
