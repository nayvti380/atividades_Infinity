contato = {}

contato['nome'] = input('Digite o seu nome: ')
contato['telefone'] = input('Digite o seu telefone: ')
contato['e-mail'] = input('Digite o seu email: ')

print( '\nInformações do Contato')
print(f'Nome: {contato['nome']}')
print(f'Telefone: {contato['telefone']}')
print(f'E-mail: {contato['e-mail']}')