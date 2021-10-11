# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o 
# carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input('Quantidade de Km percorridos pelo carro: '))
dias = int(input('Quantidade de dias em que ele foi alugado: '))
carro = 60 * dias
preçoKm = 0.15 * km
valorTot = (carro + preçoKm)
print(f'Baseando-se na Quilimetragem e Dias utilizados o valor total do alugel foi de: {valorTot}')