def maior_numero(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2>= n1 and n2 >= n3:
        return n2
    else:
        return n3
    
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero:'))
num3 = float(input('Digite o terceiro numero: '))

resultado = maior_numero(num1,num2,num3)

print('O maior numéro é :' , resultado)

