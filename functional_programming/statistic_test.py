# Import the statistics module
import statistics

# Initialize a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate the mean
mean = statistics.mean(numbers)
print("Mean:", mean)

# Calculate the median
median = statistics.median(numbers)
print("Median:", median)

# Calculate the mode (if applicable, although this list may not have a unique mode)
try:
    mode = int(statistics.mode(numbers))
    print("Mode:", mode)
except statistics.StatisticsError:
    print("Mode: No unique mode found")

# Calculate the range
range_val = max(numbers) - min(numbers)
print("Range:", range_val)

# Calculate the variance
variance = statistics.variance(numbers)
print("Variance:", variance)

# Calculate the standard deviation
std_dev = statistics.stdev(numbers)
print("Standard Deviation:", std_dev)

