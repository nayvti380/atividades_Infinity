qtd_alunos = int(input('Digite a quantidade de alunos(as): '))

for n in range(qtd_alunos):
    nome = input(f'Digite o nome do(a) {n+1}º aluno(a): ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    media = (nota1 + nota2 + nota3) /3

    if media >= 12:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    
    print('=' * 30)
    print(f'Nome do aluno(a): {nome}')
    print(f'Nota de cada semestre: {nota1}, {nota2}, {nota3}')
    print(f'Valor total das notas do aluno(a): {media}')
    print(f'O {nome} foi aprovado? {resultado}')