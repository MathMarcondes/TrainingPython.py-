print('Gerador de P.A.')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont<= 10:
    print(f'{razão}')
    termo+=razão 
    cont+=1
print('FIM')