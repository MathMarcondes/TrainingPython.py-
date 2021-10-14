#
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0<=num<=20:
        break
    print('Tente novamente')
print(f'Você digitou o número {cont[num]}')