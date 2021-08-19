def information_cars(mark, model, **info_cars):
    info_cars['mark_car'] = mark
    info_cars['model_car'] = model
    return info_cars


inf_car = information_cars('subaru', 'outback', color='blue', tow_package=True)
print(inf_car)

