def media(n1,n2,n3):
    soma = n1 + n2 + n3
    media_aritimetica = soma / 3
    return media_aritimetica

numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))
numero3 = float(input('Digite o terceiro numero: '))

resultado =  media(numero1, numero2, numero3)

print('A média dos treês números é:', resultado)

