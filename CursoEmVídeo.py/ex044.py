# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

preço = float(input('Preço das compras: '))
print('''Formas de pagamento: 
[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço formal 
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opção = int(input('Qual a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
    parcela = total / 2
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format())
print('Sua compra de R${:.2f} no final.'.format(preço, total))