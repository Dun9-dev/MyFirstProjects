file_name = '../other_files/guest_book.txt'
name = ''

with open(file_name, 'w') as file_object:
    while name != 'q':
        name = input("Введите ваше имя (для выхода введите 'q'): ")
        if name != 'q':
            file_object.write(f"{name}\n")
        elif name == '':
            print("Это не имя!")
