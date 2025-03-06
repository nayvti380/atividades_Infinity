print('Adivinhe qual é o numero')

numero_certo = 5
tentativas = 3 
contador = 0 

while contador < tentativas: 
    palpite = int(input('Digite um numero de 0 a 10: '))

    if palpite == numero_certo:
        print('Você acertou!')
        break

    elif palpite < numero_certo:
        print('O número correto é maior')
    
    elif palpite > numero_certo:
        print('O número correto é menor')

    contador += 1

else:
    print(f'Você usou todas as tentativas. O número correto era: {numero_certo}')
    print('Não fique triste! :(  Tente novamente. ')