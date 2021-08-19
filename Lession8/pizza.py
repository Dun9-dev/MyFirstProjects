def make_pizza(size, *toppings):
    """Вывод всех заказных топингов."""
    print(f"\nMaking a {size}sm pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
