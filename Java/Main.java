package Java;

class Main {
    public static void main(String[] args) {
        Car car = new Car("AMQ123", new Account("Andres Herrera", "AND123"));
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car("NAQ432", new Account("Manolo", "PLK987"));
        car2.passenger = 2;
        car2.printDataCar();
    }
}