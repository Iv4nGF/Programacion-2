class Cola:
    def __init__(self, n):
        self.n = n
        self.arreglo = [0] * n
        self.inicio = 0
        self.fin = -1
        self.cantidad_elementos = 0

    def insert(self, e):
        if self.isFull():
            print("Cola llena")
            return
        self.fin = (self.fin + 1) % self.n
        self.arreglo[self.fin] = e
        self.cantidad_elementos += 1

    def remove(self):
        if self.isEmpty():
            print("Cola vacía")
            return -1
        elemento = self.arreglo[self.inicio]
        self.inicio = (self.inicio + 1) % self.n
        self.cantidad_elementos -= 1
        return elemento

    def peek(self):
        if self.isEmpty():
            print("Cola vacía.")
            return -1
        return self.arreglo[self.inicio]

    def isEmpty(self):
        return self.cantidad_elementos == 0

    def isFull(self):
        return self.cantidad_elementos == self.n

    def size(self):
        return self.cantidad_elementos

if __name__ == "__main__":
    cola = Cola(5)
    cola.insert(10)
    cola.insert(20)
    cola.insert(30)

    print("Primer elemento (peek):", cola.peek())
    print("Eliminado:", cola.remove())
    print("Tamaño actual:", cola.size())
