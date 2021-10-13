num = int(input('Digite um valor: '))
r = 0
for c in range(1, 11):
    r = c*num
    print(f'{num}x{c}={r}')
