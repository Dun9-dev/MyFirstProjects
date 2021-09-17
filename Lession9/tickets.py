from random import choice

tickets = ['h', 'l', 'w', 'g', 5, 10, 788]
i = 0
print("Выйгрышный билет:")
while i < 4:
    print(choice(tickets))
    i += 1

