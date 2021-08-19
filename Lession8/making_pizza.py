# Варианты импортирования модуля с функциями:
# import make_pizza
# import make_pizza as p использование псевдонима для модуля
# from pizza import make_pizza
# from pizza import make_pizza as mp с использованием псевдонима для функции
from pizza import make_pizza as mp

mp(16, 'peperoni')
mp(33, 'mushrooms', 'green peperoni', 'extra cheese')
