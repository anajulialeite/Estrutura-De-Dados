filmes = {"Mad Max": {"ano": 2015, "gênero": "ação", "nota": 8.1},
         "Superbad": {"ano": 2007, "gênero": "comédia", "nota": 7.6},
         "A espera de um milagre": {"ano": 1999, "gênero": "drama", "nota": 8.6},
         "Hereditário": {"ano": 2018, "gênero": "terror", "nota": 7.3},
         "Soul": {"ano": 2020, "gênero": "animação", "nota": 8.1}}

#Acesando as informações de todos os filmes
for nome, info in filmes.items():
    print(f"{nome} - ano: {info ["ano"]}, gênero: {info["gênero"]}, nota: {info["nota"]}")
    print()

#Lista de notas
notas = [8.1, 7.6, 8.6, 7.3, 8.1]

#Calculando a média
media = sum(notas) / len(notas)

#Mostre o resultado
print(f"A média das notas é: {media:.2f}")