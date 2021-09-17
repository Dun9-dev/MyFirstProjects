class User:
    """Модель сборки данных о пользователе"""
    def __init__(self, first_name, last_name, date_registrations, nickname):
        self.full_name = f"{first_name} {last_name}"
        self.date_registrations = date_registrations
        self.nickname = nickname
        self.login_attempts = 82

    def describe_user(self):
        """Вывод данных о пользователе"""
        print(self.full_name.title())

    def greet_user(self):
        """Приветствование пользователя"""
        print(f"Hello {self.nickname}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    """Простая модель привелегий"""
    def __init__(self, privileges = "Администратор вправе удалять и добавлять пользователей, "
                                    " так же иметь всю информацию которую пользователь указал при регистрации."):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Привелегии администратора: {self.privileges}")


class Admin(User):
    """Модель администратора"""
    def __init__(self, first_name, last_name, date_registrations, nickname):
        super().__init__(first_name, last_name, date_registrations, nickname)
        self.pr = Privileges()


admin = Admin('root', '', '', 'root')
admin.pr.show_privileges()

u = User('eric', 'cartman', '18.02.2000', 'ecartman')
u.greet_user()
u.describe_user()

u.increment_login_attempts()
print(u.login_attempts)

u.reset_login_attempts()
print(u.login_attempts)

u.increment_login_attempts()
print(u.login_attempts)
