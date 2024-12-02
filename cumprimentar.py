nomes = ["Prata", "Samuel"]

def cumprimentar(nome: str):
     return f"Olá {nome}"
cumprimentos = list(map(cumprimentar, nomes))
print(cumprimentos)

