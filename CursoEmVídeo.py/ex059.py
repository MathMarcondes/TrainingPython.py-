n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print(''' 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>>>>>>> Selecione: '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma dos valores é: {soma}')
    elif opção == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação entre os números é: {multiplicar}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        novos = str('selecione novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Saiu do Programa')