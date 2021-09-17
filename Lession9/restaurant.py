class Restaurant:
    """Модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализация данных о ресторане"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_serv = 5

    def describe_restaurant(self):
        """Приветсвтие"""
        print(f"Welcome in {self.restaurant_name}!")

    def open_restaurant(self):
        """Статус ресторана"""
        print(f"\nRestaurant {self.cuisine_type}.")

    def number_served(self):
        print(f"Total served: {self.num_serv}")

    def increment_served(self, num_pl):
        """Примерное посещение в день."""
        self.num_serv += num_pl


class IceCreamStand(Restaurant):
    """Наследник класса Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = "banana"

    def flavor_print(self):
        print(f"Da, u nas morojennoe tok {self.flavors}")


f = IceCreamStand("Lamajo", "open")
f.flavor_print()

"""
restaurant_0 = Restaurant("Lamajo", "open")
restaurant_0.open_restaurant()
restaurant_0.describe_restaurant()
restaurant_0.increment_served(167)
restaurant_0.number_served()


restaurant_1 = Restaurant("Hinkali", "open")
restaurant_1.open_restaurant()
restaurant_1.describe_restaurant()
restaurant_1.increment_served(167)
restaurant_1.number_served()


restaurant_2 = Restaurant("Sushi", "open")
restaurant_2.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_2.increment_served(167)
restaurant_2.number_served()
"""