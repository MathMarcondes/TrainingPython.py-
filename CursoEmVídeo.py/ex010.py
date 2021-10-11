# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Dinheiro na carteira: '))
dol = 5.52
compra = carteira // dol
print(f'Com R${carteira} pode-se comprar U${compra}!')