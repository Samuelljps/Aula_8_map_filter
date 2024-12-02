# precos = [51, 60, 87, 93]

# valor = list(map(lambda x: x - (x * 0.10), precos))
# print(valor)

#========================================================================
# ou 
#========================================================================

precos = [100, 10, 50, 59.99]

def calcular_90_por_cento(numero: float):
    resultado = numero * 0.9
    resultado_arredondado = round(resultado, 2)
    
precos_reduzidos = list(map(lambda numero: round(numero * 0.9, 2), precos))
print(precos_reduzidos)