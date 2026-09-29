import json

alunos = {}

with open('notas.txt', 'r', encoding='utf-8') as arqNotas:
    for linha in arqNotas:
        linha = linha.strip()
        aluno = linha.split(',')
        rm = aluno[0]
        nome = aluno[1]
        notas_str = aluno[2:]
        notas = [float(nota) for nota in notas_str]
        print(rm, nome, notas)
        alunos[rm] = {'nome': nome, 'notas': notas}
print(alunos)

with open('notas.json', 'w', encoding='utf-8') as arqNotas:
    json.dump(alunos, arqNotas, indent=4, ensure_ascii=False)


