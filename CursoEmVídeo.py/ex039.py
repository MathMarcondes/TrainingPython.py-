#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou 
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos.')
if idade == 18:
    print('Meus pêsames, mas você já possui idade para se alistar.')
elif idade < 18:
    print(f'Ainda faltam {atual} anos para você se alistar')
else:
    print('Já é maior de idade e acima dos 18 anos e foi dispensado? Só agradece!')
    