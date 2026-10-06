import json
#
# alunos = {}
#
# with open('notas.txt', 'r', encoding='utf-8') as arqNotas:
#     for linha in arqNotas:
#         linha = linha.strip()
#         aluno = linha.split(',')
#         rm = aluno[0]
#         nome = aluno[1]
#         notas_str = aluno[2:]
#         notas = [float(nota) for nota in notas_str]
#         print(rm, nome, notas)
#         alunos[rm] = {'nome': nome, 'notas': notas}
# print(alunos)
#
# with open('notas.json', 'w', encoding='utf-8') as arqNotas:
#     json.dump(alunos, arqNotas, indent=4, ensure_ascii=False)

# //////////////////////////////////////////////////////////////////////

heroisVoadores = {}

# Lendo todos os heróis que possuem "Flight" como poder.
with open('heroes.json', 'r', encoding='utf-8') as arqHeroes:
    heroes = json.load(arqHeroes)
    print(type(heroes))
    print(heroes['members'])
    for member in heroes['members']:
        if 'Flight' in member['powers']:
            print(member['name'])
            heroisVoadores.update({member['name']: member['powers']})
    print(heroisVoadores)


# Escrevendo um arquivo somente com os Heróis que possuem "Flight" como poder.
with open('herois_flight.json', 'w', encoding='utf-8') as arqHerois:
    json.dump(heroisVoadores, arqHerois, indent=4, ensure_ascii=False)
