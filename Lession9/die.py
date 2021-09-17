from random import randint


class Die:
    """Модель кубика"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        if self.sides:
            print(randint(1, self.sides))
        else:
            print("У кубика 0 граней.")


die = Die(20)
die.roll_die()
