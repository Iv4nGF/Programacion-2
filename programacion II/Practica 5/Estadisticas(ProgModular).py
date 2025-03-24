import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros, prom):
    sumaCuadrados = sum((x - prom) ** 2 for x in numeros)
    return math.sqrt(sumaCuadrados / (len(numeros) - 1))

numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))

if len(numeros) != 10:
    print("Debe ingresar exactamente 10 números.")
else:
    prom = promedio(numeros)
    desviacion = desviacion(numeros, prom)

    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desviacion:.5f}")
