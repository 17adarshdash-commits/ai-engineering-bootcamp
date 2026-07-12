class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start(self):
        print(f"{self.brand} {self.model} car started.")

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def start(self):
        print(f"{self.brand} {self.model} bike started.")

car = Car("Toyota", "Camry")
bike = Bike("Royal Enfield", "Classic 350")

car.start()
bike.start()