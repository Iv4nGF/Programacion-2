import math

class Estadisticas:
    def __init__(self, numeros):
        self.numeros = numeros
    
    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        prom = self.promedio()
        sumaCuadrados = sum((x - prom) ** 2 for x in self.numeros)
        return math.sqrt(sumaCuadrados / (len(self.numeros) - 1))

numeros = list(map(float, input("Ingrese 10 números separados por espacio: ").split()))

if len(numeros) != 10:
    print("Debe ingresar exactamente 10 números.")
else:
    stats = Estadisticas(numeros)
    print(f"El promedio es {stats.promedio():.2f}")
    print(f"La desviación estándar es {stats.desviacion():.5f}")