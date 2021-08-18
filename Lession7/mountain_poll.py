responses = {}

# Устанавливаем флаг продолжения опроса
polling_active = True

while polling_active:
    # Запрос имеи и ответа у пользователя
    name = input("\nWhat is you name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Ответ сохраняться в словаре
    responses[name] = response

    # Проверка продолжения опроса
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Опрос завершенб вывести результаты.
print("\n----Poll Results----")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
