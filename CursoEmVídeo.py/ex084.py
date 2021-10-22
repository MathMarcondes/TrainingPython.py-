

pessoas = list()
n = 10
c = 0


while c < n:
    nome = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    list = (nome, peso)
    c+=1
    resp = str(input('Deseja continuar? '))
    if resp =='n':
        break
    
print(f'Ao todo {c} pessoas foram cadastradas.')

