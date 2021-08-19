def city_country(city, country):
    cc = f"{city}, {country} "
    return cc


in_city = input("Введите название города: ")
in_country = input("Введите название страны: ")
formated_cc = city_country(in_city, in_country)
print(formated_cc)
