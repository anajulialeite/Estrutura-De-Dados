estudantes = {"Ana Júlia":{"idade":32, "Telefone": 61996773513, "Nota": 10},
              "Éder":{"idade": 42, "Telefone": 61992810393, "Nota": 10,},
              "Rafael":{"idade": 23, "Telefone": 61994105407, "Nota": 9},
              "Gabriel":{"idade": 22, "Telefone": 610986025289, "Nota": 8},
              "César":{"idade":42, "Telefone": 61981826476, "Nota": 10}}

#Acessando a informação de um usuário
print(estudantes["Ana Júlia"])
print()

#Acessando as informações de todos os usuários
for nome, info in estudantes.items():
    print(f"{nome} - idade: {info["idade"]}, Nota: {info["Nota"]}")
    print()

soma_notas = 0
contador_estudantes = 0

#Somar as notas 
for info in estudantes.values():
    soma_notas += info["Nota"]
    contador_estudantes += 1
print(f"A soma das notas é: {soma_notas}")#não colocar dentro do for

#Média dos alunos
if contador_estudantes > 0:
    media = soma_notas / contador_estudantes
    print(f"A média das notas é: {media}")
else:
    print("Nenhum estudante encontrado.")
