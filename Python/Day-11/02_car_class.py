class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year =  year

    def start_engine(self):
        print(f"{self.year} {self.brand} {self.model} engine started!")

car1 = Car("Lamborghini", "Aventador", 2026)
car1.start_engine()