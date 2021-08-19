def print_models(unprinted_design, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Вывод всех готовых моделей"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# Список моделей, которые необходимо напечатать
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)
