# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Digite o valor da largura: '))
alt = float(input('Digite o valor da altura: '))
area = larg*alt
litro = area/2
print(f'A área total da parede é de {area}, fazendo assim a litragem a ser gasta de tinta é de: {litro}L')
