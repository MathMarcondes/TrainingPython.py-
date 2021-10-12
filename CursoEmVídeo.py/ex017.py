# Faça um programa que leia o comprimento do cateto oposto e do cateto 
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da 
# hipotenusa.


co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (ca**2 + co**2) ** (1/2)
print('A soma do quadrado dos catetos é {:.2f}'.format(hi)) 