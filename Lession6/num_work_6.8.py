# Упражнение 6.8
animals = {
    'bella': {
        'breed': 'british',
        'age': 4,
        'owner': 'carl'
    },
    'alfie': {
        'breed': 'british longhair',
        'age': 7,
        'owner': 'jhone'
    },
    'coco': {
        'breed': 'burmilla',
        'age': 13,
        'owner': 'ivan'
    }
}

for pet_name, pet_info in animals.items():
    print(f"This pet's name{pet_name.title()}. And here is some data about it:")
    print(f"\tIts breed: {pet_info['breed'].title()}\n\tIt: {pet_info['age']} age\n\tIts owner: {pet_info['owner'].title()}")

