class Animal():
    def speak(self):
        print("Animal makes a sound.")

class Lion(Animal):
    def speak(self):
        print("Lion roars!")

class Elephant(Animal):
    def speak(self):
        print("Elephant trumpets!")

class Monkey(Animal):
    def speak(self):
        print("Monkey chatters!")

lion = Lion()
elephant = Elephant()
monkey = Monkey()

animals = [lion, elephant, monkey]
for animal in animals:
    animal.speak()