# Упражнение 6.7
people = [{
    'first_name': 'jhon',
    'last_name': 'williams',
    'age': 25,
    'city': 'NY',
    },
    {
    'first_name': 'adam',
    'last_name': 'capones',
    'age': 32,
    'city': 'VC',
    },
    {
    'first_name': 'carl',
    'last_name': 'jonson',
    'age': 17,
    'city': 'SW',
    }]

print(people)

for i in people:
    # Запись имени и фамилии в одну переменную
    fullname = f"{i['first_name']} {i['last_name']}"
    print(f"\n{fullname.title()}\nПолных лет: {i['age']}\nПроживает в городе: {i['city'].upper()}")
