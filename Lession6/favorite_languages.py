favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

names = ['ivan', 'carl', 'phil', 'watson']

for name in names:
    if name not in favorite_languages:
        print(f"Добрый день, предлагаю вам пройти опрос {name.title()}")
    else:
        print(f"{name.title()}, Спасибо что прошли опрос!")

