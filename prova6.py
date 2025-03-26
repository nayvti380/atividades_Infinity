print('Seja Bem-Vindo')
print('-'*100)
tentavivas = 0 

while tentavivas < 3:
    login = input('Digite o seu Login: ')
    senha = input('Digite a sua senha: ')

    if login == 'Admin1252' and senha == 'Gestão1252':
        print('Acesso Liberado')
        break

    else: 
        tentavivas += 1
        tentavivas_restantes = 3 - tentavivas
        if tentavivas > 0:
            print(f'Acesso negado, você tem {tentavivas_restantes} tentativas restantes.')
        else:
            print('Acesso negado, você não tem mais tentativas.')
if tentavivas == 3:
    print('Acesso bloqueado, recupere a sua conta.')
    
print('Fim!')

