# Crie um programa que vai ler vários números e colocar em uma lista.
# 
# Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    valores.append(int(input('Digite algum valor: '))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break

print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescete são {valores}')