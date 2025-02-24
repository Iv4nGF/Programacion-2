public class Circulo {
    public static class Punto {
        public int x;
        public int y;

        public Punto(int xValor, int yValor) {
            x = xValor;
            y = yValor;
        }

        public String toString() {
            return x + ", " + y;
        }
    }

    public Punto centro;
    public float radio;

    public Circulo(Punto c, float r) {
        centro = c;
        radio = r;
    }

    public String toString() {
        return "Circulo(" + centro + ", radio=" + radio + ")";
    }

    public void dibujaCirculo() {
        System.out.println("Dibujando un círculo en " + centro + " con radio " + radio);
    }

    public static void main(String[] args) {
        Circulo.Punto centro = new Circulo.Punto(5, 10);
        Circulo circulo = new Circulo(centro, 3.5f);
        System.out.println(circulo);
        circulo.dibujaCirculo();
    }
}