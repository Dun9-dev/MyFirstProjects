def addition(first_num, second_num):
    try:
        i = int(first_num)
        k = int(second_num)
        print(i+k)
    except ValueError:
        print('ti loh, eto ne 4islo')


while True:
    print("Введите 'q' чтобы выйти.")
    i = input('Введите первоче число: ')
    k = input('Введите второе число: ')
    if i == 'q' or k == 'q':
        break
    else:
        addition(i, k)

