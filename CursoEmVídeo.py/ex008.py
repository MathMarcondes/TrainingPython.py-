# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

x = float(input('Digite um valor em metros: '))
m = x
c = m*100
mm = c*100
print(f'{m}m; {c}cm; {mm}mm')