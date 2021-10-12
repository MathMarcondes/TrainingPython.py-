# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Digite a distância da viagem: '))
valor = dist * 0.50 if dist <= 200 else dist * 0.45
print('O valor da passagem ficará: {:.2f}'.format(valor))