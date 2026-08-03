class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def display_info(self):
        print(f"Car: {self.brand}, Engine: {self.engine.horsepower} HP")

    def start(self):
        self.engine.start()


if __name__ == "__main__":
    engine = Engine(150)
    car = Car("Toyota", engine)

    car.display_info()
    car.start()
