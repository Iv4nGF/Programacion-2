public class Linea {
    public static class Punto {
        float x, y;

        Punto(float a, float b) {
            x = a;
            y = b;
        }

        float[] coord_cartesianas() {
            return new float[]{x, y};
        }

        double[] coord_polares() {
            double r = Math.sqrt(x * x + y * y);
            double theta = Math.atan2(y, x);
            return new double[]{r, theta};
        }

        public String toString() {
            return x + ", " + y;
        }
    }

    Punto p1, p2;

    Linea(Punto punto1, Punto punto2) {
        p1 = punto1;
        p2 = punto2;
    }

    public String toString() {
        return "Linea = " + p1 + " Punto " + p2;
    }

    void dibujaLinea() {
        System.out.println("Dibujando una línea desde " + p1 + " hasta " + p2);
    }

    public static void main(String[] args) {
        Punto p1 = new Punto(1, 2);
        Punto p2 = new Punto(3, 4);
        Linea linea = new Linea(p1, p2);

        System.out.println(linea);
        linea.dibujaLinea();
    }
}
