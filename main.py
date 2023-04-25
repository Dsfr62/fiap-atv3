def custo_mensal(n:int):
    return 9500 + (680*n)

def receita_mensal(n:int):
    venda = 940 - n
    return venda * n

def lucro_mensal(n:int):
    return receita_mensal(n) - custo_mensal(n)

resultados = []
contador = 0

while contador <= 940:
    resultado = lucro_mensal(contador)
    if "-" in str(resultado):
        print(f"Passou: {contador}")
    else:
        print(f"Adicionou: {contador}")
        resultados.append({"n": contador, "lucro_maximo": resultado})
    
    contador += 1

print(f"\n{resultados}")
