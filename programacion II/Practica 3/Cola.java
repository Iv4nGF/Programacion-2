import java.util.Scanner;

public class Cola {
    private long[] arreglo;
    private int inicio, fin, n, cantidadElementos;

    public Cola(int n) {
        this.n = n;
        arreglo = new long[n];
        inicio = 0;
        fin = -1;
        cantidadElementos = 0;
    }

    public void insert(long e) {
        if (isFull()) {
            System.out.println(" Cola llena.");
            return;
        }
        fin = (fin + 1) % n;
        arreglo[fin] = e;
        cantidadElementos++;
        System.out.println(" Insertado: " + e);
    }

    public long remove() {
        if (isEmpty()) {
            System.out.println(" Cola vacía.");
            return -1;
        }
        long elemento = arreglo[inicio];
        inicio = (inicio + 1) % n;
        cantidadElementos--;
        System.out.println(" Eliminado: " + elemento);
        return elemento;
    }

    public long peek() {
        return isEmpty() ? -1 : arreglo[inicio];
    }

    public boolean isEmpty() {
        return cantidadElementos == 0;
    }

    public boolean isFull() {
        return cantidadElementos == n;
    }

    public int size() {
        return cantidadElementos;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("tamaño de cola: ");
        int tamano = scanner.nextInt();
        Cola cola = new Cola(tamano);

        cola.insert(10);
        cola.insert(20);
        cola.insert(30);
        cola.insert(40);
        cola.insert(50);

        System.out.println(" Primer elemento (peek): " + cola.peek());
        cola.remove();
        cola.remove();
        System.out.println(" Tamaño actual de la cola: " + cola.size());
        cola.insert(60);
        cola.insert(70);

        scanner.close();
    }
}
