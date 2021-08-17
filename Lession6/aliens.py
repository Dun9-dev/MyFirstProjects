# Создание пустого списка для хранения прешельцев
aliens = []

# Создание 30ти зеленых пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Трансформация первых трех пришельцев
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Вывод первых 5ти пришельцев
for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")
