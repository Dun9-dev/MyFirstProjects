class User:
    """Модель сборки данных о пользователе"""
    def __init__(self, first_name, last_name, date_registrations, nickname):
        self.full_name = first_name + last_name
        self.date_registrations = date_registrations
        self.nickname = nickname

    def describe_user(self):
        """Вывод данных о пользователе"""
        print(self.first_name)

    def greet_user(self):
        """Приветствование пользователя"""
        print(f"Hello {self.nickname}")


u = User('eric', 'cartman', '18.02.2000', 'ecartman')
u.greet_user()
