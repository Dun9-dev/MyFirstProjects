class Dog:
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садитсья по команде"""
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('luci', 3)

print(f"My dog`s name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog`s name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
