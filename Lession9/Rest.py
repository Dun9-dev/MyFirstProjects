class Restaurant:
    """Модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"Restic {self.restaurant_name}, open")


res = Restaurant('test_name', 'eeeee')
res.open_restaurant()
res.describe_restaurant()
