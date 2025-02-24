public class Punto {
    private final double x;
    private final double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double[] coordCartesianas() {
        return new double[]{x, y};
    }

    public double[] coordPolares() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.atan2(y, x);
        return new double[]{r, theta};
    }

    @Override
    public String toString() {
        return "Punto(" + x + ", " + y + ")";
    }

    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println("Coordenadas Cartesianas: " + java.util.Arrays.toString(p.coordCartesianas()));
        System.out.println("Coordenadas Polares: " + java.util.Arrays.toString(p.coordPolares()));
        System.out.println("Representación del Punto: " + p);
    }

    public double getX() {
        return x;
    }
}

