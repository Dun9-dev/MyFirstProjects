import json


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = f'../other_files/json_file/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя"""
    username = input("What is your name?\n")
    filename = '../other_files/json_file/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We`ll remember you when you come back, {username}!")


with open('../other_files/json_file/username.json') as f:
    name = json.load(f)
print(f"Ваше имя {name}?")
print("Если да то '+'\nЕсли нет, то '-'\n")
i = input()
if i == '+':
    greet_user()
elif i == '-':
    get_new_username()


