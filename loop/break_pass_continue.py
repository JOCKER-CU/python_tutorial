
#break statement

def break_example():
    for i in range(10):
        if i == 5:
            break
        print(i)
print("--------")
break_example()

#continue statement

def continue_example():
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)

print("--------")

continue_example()

#pass statement

def pass_example():
    for i in range(10):
        if i % 2 == 0:
            print(i, 'in pass statement executed')

            pass
            print(i, 'after pass statement executed')
        # print(i, 'outer statement executed')

print("--------")

pass_example()