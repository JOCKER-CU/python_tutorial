
# Data Type Conversion

# Integer conversions
print("Integer conversions:")
integer = 42
print(f"Original integer: {integer}")
float_from_int = float(integer)
print(f"Integer to float: {float_from_int}")
string_from_int = str(integer)
print(f"Integer to string: {string_from_int}")
bool_from_int = bool(integer)
print(f"Integer to boolean: {bool_from_int}")

print("\n" + "=" * 30 + "\n")

# Float conversions
print("Float conversions:")
float_num = 3.14
print(f"Original float: {float_num}")
int_from_float = int(float_num)
print(f"Float to integer: {int_from_float}")
string_from_float = str(float_num)
print(f"Float to string: {string_from_float}")
bool_from_float = bool(float_num)
print(f"Float to boolean: {bool_from_float}")

print("\n" + "=" * 30 + "\n")

# String conversions
print("String conversions:")
string = "123"
print(f"Original string: {string}")
int_from_string = int(string)
print(f"String to integer: {int_from_string}")
float_from_string = float(string)
print(f"String to float: {float_from_string}")
bool_from_string = bool(string)
print(f"String to boolean: {bool_from_string}")

print("\n" + "=" * 30 + "\n")

# Boolean conversions
print("Boolean conversions:")
boolean = True
print(f"Original boolean: {boolean}")
int_from_bool = int(boolean)
print(f"Boolean to integer: {int_from_bool}")
float_from_bool = float(boolean)
print(f"Boolean to float: {float_from_bool}")
string_from_bool = str(boolean)
print(f"Boolean to string: {string_from_bool}")

print("\n" + "=" * 30 + "\n")

# List, tuple, and set conversions
print("List, tuple, and set conversions:")
my_list = [1, 2, 3]
print(f"Original list: {my_list}")
tuple_from_list = tuple(my_list)
print(f"List to tuple: {tuple_from_list}")
set_from_list = set(my_list)
print(f"List to set: {set_from_list}")

my_tuple = (4, 5, 6)
print(f"\nOriginal tuple: {my_tuple}")
list_from_tuple = list(my_tuple)
print(f"Tuple to list: {list_from_tuple}")
set_from_tuple = set(my_tuple)
print(f"Tuple to set: {set_from_tuple}")

my_set = {7, 8, 9}
print(f"\nOriginal set: {my_set}")
list_from_set = list(my_set)
print(f"Set to list: {list_from_set}")
tuple_from_set = tuple(my_set)
print(f"Set to tuple: {tuple_from_set}")
