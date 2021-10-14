#
total = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço 


    res = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [N/S] ')).upper().strip()
    if resp == 'N':
        break 
print('{:-^40}'.format('Fim do Programa'))
print('O valor total da compra foi de: R${total:10.2f};')