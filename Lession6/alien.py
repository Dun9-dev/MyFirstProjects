alien_0 = {'color': 'green', 'points': 5, 'x_position': 5, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Пришелец перемещается вправо
# Вычисляем величину смещения на основании текущей скорости

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3

# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] += x_increment

print(f"New position: {alien_0['x_position']}")

del alien_0['points']
print(alien_0)
