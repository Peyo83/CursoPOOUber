from car import Car

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car()
    car.license = "ADFR222"
    car.driver = "Paco"
    print(vars(car))

    car2 = Car()
    car2.license = "PRD432"
    car2.driver = "Luis"
    print(vars(car2))