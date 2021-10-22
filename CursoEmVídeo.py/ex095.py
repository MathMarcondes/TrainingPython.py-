


time = list()
jogador = dict()
partidas = list()
while True: 
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} realizou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na {c+1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
            print('Responda apenas com "S" ou "N".')
    if resp == 'N':
        break
print('=-'*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}')
print()
print('=-'*30)

for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()




print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' -> Na partida {i}, fez {v} gols.')
    print(f'Foi um total de {jogador["total"]} gols.')

print('=-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')