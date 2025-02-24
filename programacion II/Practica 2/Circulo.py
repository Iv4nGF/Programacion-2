class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return "Circulo({}, {}, radio={})".format(self.centro.x, self.centro.y, self.radio)

    def dibuja_circulo(self):
        print("Dibujando un círculo en {} con radio {}".format(self.centro, self.radio))

centro = Punto(5, 10)
circulo = Circulo(centro, 3.5)
print(circulo)
circulo.dibuja_circulo()
