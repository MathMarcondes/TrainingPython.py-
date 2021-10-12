#Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

name = str(input('Digite seu nome completo: ')).strip()
print(name.lower())
print(name.upper())
print(len(name))

print('O primeiro nome tem: ')
print(name.find(' '))
separa = name.split()
print('Seu primeiro nome é {} e ele tem {}'.format(separa[0], len(separa[0])))