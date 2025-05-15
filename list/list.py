my_List = list()
print(my_List)

my_List.append(1)
print(my_List)

b_list = []
print(b_list)

my_List.append(range(0,10));
b_list = my_List.copy()
print(b_list)

a_list = []
a_list.extend(range(0,10))

print(a_list)
print(a_list[:2])

any_list = ['Aung Aung', 123, True, [1, 2, 3]];

print(any_list);

print('\n');
for item in any_list:
    print(item)

print( type(any_list))
print(len(any_list), "elements")

name = list('Aung Aung');
print(name);

print(any_list +  b_list);

alpha_list = ['a', 'b', 'c', 'z', 'y', 'x', 'm', 'n', 'p', 'q', 'r', 't', 'v', 'w', 's', 'j', 'k', 'l', 'i', 'h',];
alpha_list.sort();
# alpha_list.sort(reverse=True);

print(alpha_list);