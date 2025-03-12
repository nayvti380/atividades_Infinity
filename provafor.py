inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))

soma = 0 

for n in range(inicio, fim+1):
    if n % 2 == 0:
        soma += n
if soma == 0:
    print('A soma total não é par.')

else:
    print(f'A soma total é par, o total é: {soma}')
