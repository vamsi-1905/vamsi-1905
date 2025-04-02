
class Vehicle {

void fuelType() {

System.out.println("Uses petrol or diesel.");

}

}


class Car extends Vehicle {

void wheels() {

System.out.println("Has 4 wheels.");

}

}


class ElectricCar extends Car {

void battery() {

System.out.println("Runs on electricity.");

}

}


public class InheritanceExample {

public static void main(String[] args) {

ElectricCar tesla = new ElectricCar();

tesla.fuelType(); // Inherited from Vehicle

tesla.wheels(); // Inherited from Car

tesla.battery(); // Defined in ElectricCar

}

}