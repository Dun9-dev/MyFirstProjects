import json

numbers = [2, 3, 4, 5, 6, 7, 8, 9]

filename = 'number.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
    
