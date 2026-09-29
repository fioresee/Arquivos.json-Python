# JSON
# Para tratar arquivos json, o python tem uma biblioteca própria

# Arquivos JSON são textos estruturados


pessoa = {'nome': 'Arthur', 'idade': 18, 'hobbies': ['caminhada', 'tenis']}
print(type(pessoa))
print(pessoa)

# A biblioteca json vai pegar esse dicionário e transformar em um texto
# Na hora de gravar um arquivo, é preciso de um texto

import json

# O metodo dumps, da biblioteca json, converte uma coleção em um texto

pessoa2 = json.dumps(pessoa)
print(type(pessoa2))
print(pessoa2)

# O uso mais comum, no entanto, é gravar essas informações em um arquivo
# O metodo agora muda de nome: dump

with open("alunos.json", 'w', encoding='utf-8') as arqAlunos:
    json.dump(pessoa, arqAlunos)
    arqAlunos.write('\n')

with open("alunos2.json", 'a', encoding='utf-8') as arqAlunos:
    json.dump(pessoa, arqAlunos, indent=4)


# Acentuação
print('\n')
print("Acentuação")
pessoanova = {'nome': 'João Alvarez', 'idade': 43, 'hobbies': ['caçada de formiga', 'tenis']}

print("Sem o parâmetro ensure_ascii=False")
pessoanova2 = json.dumps(pessoanova, indent=4)
print(type(pessoanova2))
print(pessoanova2)


print("Com o parâmetro ensure_ascii=False")
pessoanova2 = json.dumps(pessoanova, indent=4, ensure_ascii=False)
print(type(pessoanova2))
print(pessoanova2)

with open ("alunos3.json", 'a', encoding='utf-8') as arqAlunos:
    arqAlunos.write('\n')
    json.dump(pessoanova, arqAlunos, indent=4, ensure_ascii=False)


alunos = {
    13923842373: {'nome': 'Arthur', 'idade': 18, 'hobbies': ['caminhada', 'tenis']},
    98465774850: {'nome': 'João Alvarez', 'idade': 43, 'hobbies': ['caçada de formiga', 'tenis']}
}

with open('todosalunos.json', 'w', encoding='utf-8') as arqAlunos:
    json.dump(alunos, arqAlunos, indent=4, ensure_ascii=False)

print("\n\nLeitura JSON")
# Enquanto o dumps (string) / dump (arquivo) escreve no formato JSON,
# o loads (string) / load(arquivo) lê do formato JSON e coloca numa coleção.

pessoatexto = '{"nome": "Antônio", "idade": 25, "hobbies": ["aeromodelismo", "board games"]}'
print(type(pessoatexto))
print(pessoatexto)

# O metodo LOADS transforma essa string em uma coleção.

pessoadicionario = json.loads(pessoatexto)
print(type(pessoadicionario))
print(pessoadicionario)

# Como ler de um arquivo? metodo LOAD

with open("alunos.json", 'r', encoding='utf-8') as arqAlunos:
    aluno = json.load(arqAlunos)
    print(type(aluno))
    print(aluno)

# DUMPS(string - texto de tela) E DUMP(arquivo) - Transformam uma coleção em texto JSON
# LOADS(string - texto de tela) E LOAD(arquivo) - Transformam um texto em uma coleção