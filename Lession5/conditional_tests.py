car = "sUbaru"
print("Is car == \"subaru\"? I predict True.")
print(car.lower() == "subaru")

print("\nIs car == \"subaru\"? I predict False.")
print(car == "audi")

price = 20999
print("\nIs price == \"20999\"? I predict True.")
print(price == 20999)

print("\nIs price == \"20999\"? I predict False.")
print(price == 20998)

print("\nIs price >= \"20999\"? I predict True.")
print(price >= 20999)

print("\nIs price <= \"20999\"? I predict True.")
print(price <= 20999)

print("\nIs price < \"20999\"? I predict True.")
print(price < 21000)

print("\nIs price > \"20999\"? I predict False.")
print(price < 2500)

age = 22
if age > 21 and age < 25:
    print("age ot 21 do 25 ")
else:
    print(False)

cars = ['bmw', 'audi', 'subaru', 'jeep']
car = "jeep"
if car in cars:
    print(f"{car.title()} in spiske")
elif car not in cars:
    print(f"{car.title()} ne in spiske")