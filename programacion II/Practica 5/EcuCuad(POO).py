import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getRaiz1(self):
        Discriminante = self.getDiscriminante()
        if Discriminante >= 0:
            return (-self.b + math.sqrt(Discriminante)) / (2 * self.a)
        return None

    def getRaiz2(self):
        Discriminante = self.getDiscriminante()
        if Discriminante > 0:
            return (-self.b - math.sqrt(Discriminante)) / (2 * self.a)
        return None

    def resolver(self):
        Discriminante = self.getDiscriminante()
        
        if Discriminante > 0:
            r1 = self.getRaiz1()
            r2 = self.getRaiz2()
            print(f"La ecuación tiene dos raíces {r1:.6f} y {r2:.6f}")
        elif Discriminante == 0:
            r1 = self.getRaiz1()
            print(f"La ecuación tiene una raíz {r1:.6f}")
        else:
            print("La ecuación no tiene raíces reales")


a, b, c = map(float, input("Ingrese a, b, c: ").split())
ecuacion = EcuacionCuadratica(a, b, c)
ecuacion.resolver()