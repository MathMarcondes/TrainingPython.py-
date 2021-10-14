print('{:^30}'.format('Banco CEV'))

valor = int(input('Que valor você quer sacar? '))
total = valor
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total-=céd
        totalcéd+=1
    else: 
        print(f'Total de {total} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
        else:
            print('Já era')
