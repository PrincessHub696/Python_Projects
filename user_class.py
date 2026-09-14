class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привет, меня зовут {self.name}! Мне {self.age} лет.")

user1 = User("Анна", 20)
user2 = User("Светлана", 48)

print(user1.name)
print(user2.age)
user1.greet()
user2.greet()