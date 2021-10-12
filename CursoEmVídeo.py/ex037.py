# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} Número convertido para Binário {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Número convertido para Octal {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Número convertido para Hexadecimal {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')
