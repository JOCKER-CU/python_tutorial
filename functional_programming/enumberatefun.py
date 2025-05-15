#enumeration


list1 = ['Apples', 'Orange', 'Mangoes','Pineapple', ]

for i, j in enumerate(list1):
    print(f'{i+1}. {j}')


dict = dict(enumerate(list1))

print('\nDictionary:')

for i, j in dict.items():
    print(f'{i+1}. {j}')

print('\nDictionary:', dict)