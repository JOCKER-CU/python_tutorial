

age = int(input("How old are you?: "));

if age >= 18:
    print("You are an adult.");
    print("You can vote.");
    print("You can hold a driving license.");
elif age < 18:
    print("You are a minor.");
    if age < 13:
        print("You cannot vote.");
        print("You cannot hold a driving license.");
    else:
        print("You can vote.");
        print("You can hold a driving license.");