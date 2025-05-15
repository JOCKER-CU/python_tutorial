
#set
my_set = {1,2,3,4,5}

print(my_set)
print(type(my_set))
print(len(my_set))
print(1 in my_set)
print(6 in my_set)

new_set = set();
print(type(new_set));

old_set = set([6,7,8,9,10]);
print(old_set);

two_sets = my_set.union(old_set);
diff_sets = my_set.difference(old_set);
inter_sets = {1,2,3,4,5}.intersection({4,5,6,7,8,9,10});

print(inter_sets, 'Intersection');

print(diff_sets, 'Difference');

print(two_sets, 'Union');

my_set.add(6);

print(my_set, 'After add'  );

my_set.remove(6);

print(my_set, 'After remove'  );

my_set.discard(7);

print(my_set, 'After discard'  );

my_set.clear();

print(my_set, 'After clear' );

print(len(my_set), 'After clear'  );

my_set = {1,2,3,4,5}

my_set.update({6,7,8,9,10});

print(my_set, 'After update'  );


my_list = [1,1,1,1,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5];

my_set = set(my_list);

print(my_set, 'After convert list to set'  );


my_set = {1,2,3,4,5,6,7,8,9,0}

print(my_set, 'Set from range'  );

my_set = {i for i in range(10) if i % 2 == 0}

print(my_set, 'Set comprehension'  );