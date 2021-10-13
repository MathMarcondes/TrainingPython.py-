# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
frase = str(input('Digite umva frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    print(junto[letra])
print(junto, inverso)
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo.')