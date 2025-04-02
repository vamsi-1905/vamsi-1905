import java.util.Scanner;

class Shape {
    int no_of_sides;

    void calculate_area() {
        System.out.println("Area calculation depends on the shape.");
    }

    void find_perimeter() {
        System.out.println("Perimeter calculation depends on the shape.");
    }
}

class Circle extends Shape {
    double radius;

    Circle(double radius) {
        this.radius = radius;
        this.no_of_sides = 0;
    }

    void calculate_area() {
        System.out.println("Area of Circle: " + (Math.PI * radius * radius));
    }

    void find_perimeter() {
        System.out.println("Perimeter of Circle: " + (2 * Math.PI * radius));
    }
}

class Rectangle extends Shape {
    double width, height;

    Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
        this.no_of_sides = 4;
    }

    void calculate_area() {
        System.out.println("Area of Rectangle: " + (width * height));
    }

    void find_perimeter() {
        System.out.println("Perimeter of Rectangle: " + (2 * (width + height)));
    }
}

public class ShapeDemo {
    public static void main(String[] args) {
        Circle c = new Circle(5.0);
        c.calculate_area();
        c.find_perimeter();

        Rectangle r = new Rectangle(4.0, 6.0);
        r.calculate_area();
        r.find_perimeter();
    }
}