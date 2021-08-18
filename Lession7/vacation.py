responses = {}

# Устанавливаем флаг продолжения опроса
polling_active = True

while polling_active:
    # Запрос имеи и ответа у пользователя
    name = input("\nКак вас зовут? ")
    response = input("Где вы бы хотели провести свой отпуск? ")

    # Ответ сохраняться в словаре
    responses[name] = response

    # Проверка продолжения опроса
    repeat = input("Вы хотите пройти опрос (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Опрос завершенб вывести результаты.
print("\n----Poll Results----")
for name, response in responses.items():
    print(f"{name.title()} провел бы отпуск в {response}.")
