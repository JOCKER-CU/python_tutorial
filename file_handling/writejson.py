import json

data = { 'name': 'Mg Oo', 'age': 25, 'city': 'New York'};

with open('file_handling\data.json', 'w') as file:
    json.dump(data, file)

with open('file_handling\data.json', 'r') as file:
    data = json.load(file)
    print(data)