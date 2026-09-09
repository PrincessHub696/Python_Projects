class Animal:  # Родительский класс
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} издаёт звук.")

class Dog(Animal):  # Дочерний класс
    def speak(self):
        print(f"{self.name} говорит: Гав-гав!")

class Cat(Animal):  # Дочерний класс
    def speak(self):
        print(f"{self.name} говорит: Мяу-мяу!")

Animal1 = Animal("Животное")
Dog1 = Dog("Бобик")
Cat1 = Cat("Мурка")

Animal1.speak()
Dog1.speak()
Cat1.speak()