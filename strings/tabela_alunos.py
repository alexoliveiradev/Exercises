"""
Faça um programa para ler uma tabela contendo os nomes dos alunos de uma turma de
5 alunos. O programa deve solicitar ao usuário os nomes do aluno, sempre perguntando
se ele deseja inserir mais um nome na lista. Uma vez lidos todos os alunos, o usuário
irá indicar um nome que ele deseja verificar se está presente na lista, onde o programa
deve procurar pelo nome (ou parte deste nome) e se encontrar deve exibir na tela o nome
completo e o ı́ndice do vetor onde está guardado este nome.
"""


def encontra_nome(nome, list_de_nomes):
    for i in list_de_nomes:
        if nome in i:
            return f'Nome: {i}, Índice: {list_de_nomes.index(i)}'


def cadastra_aluno():
    lista_alunos = list()
    while True:
        nome_aluno = str(input(f'Nome do {len(lista_alunos) + 1}º aluno: '))
        lista_alunos.append(nome_aluno)
        if len(lista_alunos) == 5:
            break
        else:
            saida = str(input('Deseja adicionar outro aluno? (S/N): ')).lower()
            if saida == 'n':
                break
            else:
                continue
    procura_aluno = str(input('Para pesquisar digite o nome do aluno:\n'))
    return encontra_nome(procura_aluno, lista_alunos)


print(cadastra_aluno())
