
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'};
print(my_dict['name']);


my_dict['city'] = 'Tokyo';
print(my_dict['city']);

my_dict['hobbies'] = ['reading', 'painting'];

print(my_dict['hobbies']);

# Delete key-value pair

del my_dict['age'];
print(my_dict);

# Check if key exists
if 'age' in my_dict:
    print('Age exists in dictionary')
elif 'weight' in my_dict:
    print('Weight exists in dictionary')
elif 'occupation' not in my_dict:
    print('Occupation does not exist in dictionary')
elif 'name' not in my_dict:
    print('Name does not exist in dictionary')
elif 'hobbies' not in my_dict:
    print('Hobbies does not exist in dictionary')
else:
    print('Neither age nor weight exists in dictionary')

new_dict=my_dict.copy()
print(new_dict)

# Iterate over dictionary

for key, value in my_dict.items():
    print(f'{key}: {value}')

# Get all keys

keys = my_dict.keys();
print(keys)

# Get all values

values = my_dict.values();
print(values)

# Get length of dictionary

print(len(my_dict))

# Merge two dictionaries

new_dict.update({'occupation': 'Engineer'})
print(new_dict)

# Clear dictionary

new_dict.clear()
print(new_dict)

# Check if dictionary is empty

if len(new_dict) == 0:
    print('Dictionary is empty')
else:
    print('Dictionary is not empty')

# Nested dictionary

nested_dict = {
    'person': {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    },
    'hobbies': ['reading', 'painting']
}

print(nested_dict['person']['name'])

# Nested dictionary with default value

nested_dict_default = {
    'person': {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    },
    'hobbies': ['reading', 'painting']
}

print(nested_dict_default.get('person', {}).get('name', 'Unknown'))

# Nested dictionary with default value and update

nested_dict_default.setdefault('person', {}).update({'name': 'Jane'})
print(nested_dict_default['person']['name'])

# Nested dictionary with default value and update

nested_dict_default.setdefault('address', {}).update({'city': 'Tokyo'})
print(nested_dict_default['address'].get('city', 'Unknown'))
print(nested_dict_default)

