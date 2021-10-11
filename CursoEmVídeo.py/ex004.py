# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite qualquer coisa: ')
print(f'O valor primitivo do que foi digitado é: {x}', type(x))
print(f'Tem espaços? ', x.isspace())
print(f'É um número? ', x.isalnum())
print(f'Está em letras minusculas? ', x.islower())
print(f'Está em letras maiúsculas? ', x.isupper())
