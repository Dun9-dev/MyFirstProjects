"""Набор классов дял представления электромобилей."""

from car import Car


class Battery:
    """Модель аккумулятора."""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            rag = 260
        elif self.battery_size == 100:
            rag = 315

        print(f"This car can go about {rag} miles on a full charge.")

    def update_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
        print(self.battery_size)


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
