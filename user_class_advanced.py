class User:
    species = "Человек"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привет, меня зовут {self.name}!")

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

user1 = User("Анна", 27)
print(user1)