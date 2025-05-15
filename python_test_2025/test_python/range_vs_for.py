import time

# Using range
start = time.time()
for i in range(1000000):
    pass
print("Using range:", time.time() - start)

# Using a pre-created list
my_list = list(range(1000000))
start = time.time()
for i in my_list:
    pass
print("Using pre-created list:", time.time() - start)
