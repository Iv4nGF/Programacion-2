import math

def getDiscriminante(a, b, c):
    return b ** 2 - 4 * a * c

def getRaiz1(a, b, Discriminante):
    return (-b + math.sqrt(Discriminante)) / (2 * a)

def getRaiz2(a, b, discriminante):
    return (-b - math.sqrt(discriminante)) / (2 * a)

def ecuacion(a, b, c):
    Discriminante = getDiscriminante(a, b, c)
    
    if Discriminante > 0:
        r1 = getRaiz1(a, b, Discriminante)
        r2 = getRaiz2(a, b, Discriminante)
        print(f"La ecuación tiene dos raíces {r1:.6f} y {r2:.6f}")
    elif Discriminante == 0:
        r1 = getRaiz1(a, b, Discriminante)
        print(f"La ecuación tiene una raíz {r1:.6f}")
    else:
        print("La ecuación no tiene raíces reales")

a, b, c = map(float, input("Ingrese a, b, c: ").split())
ecuacion(a, b, c)