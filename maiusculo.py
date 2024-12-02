nomes = ["Prata", "Samuel"]
for i in range(0,2):
    nomes[i] = nomes[i].upper()
print(nomes)

deixar_maiusculo = lambda x: x.upper()
nomes_maiusculos = list(map(deixar_maiusculo, nomes))
print(nomes_maiusculos)
