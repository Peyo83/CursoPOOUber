from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")

    car = Car("ADFR222", Account("Paco", "ANDF44"))
    print(vars(car))
    print(vars(car.driver))