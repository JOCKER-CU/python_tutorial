#advanced list

list1 = list(range(1, 10))
list2 = list(range(11,20))


list1.extend(list2)

print('Extended list:', list1)

#merge lists

merged_list = list1 + list2

print('Merged list:', merged_list)

#sort list

sorted_list = sorted(merged_list)

print('Sorted list:', sorted_list)

#remove duplicates

unique_list = list(set(sorted_list))

print('Unique list:', unique_list)

#find sum

sum_of_elements = sum(unique_list)

print('Sum of elements:', sum_of_elements)

#find average

average = sum_of_elements / len(unique_list)

print('Average:', average)

#find maximum   

max_element = max(unique_list)

print('Maximum element:', max_element)

#find minimum

min_element = min(unique_list)

print('Minimum element:', min_element)

#find median

sorted_list.sort()

if len(sorted_list) % 2 == 0:
    median = (sorted_list[len(sorted_list) // 2 - 1] + sorted_list[len(sorted_list) // 2]) / 2
else:
    median = sorted_list[len(sorted_list) // 2]

print('Median:', median)

#find mode

# mode_count = sorted(list(set(unique_list)), key=unique_list.count)[-1]

# print('Mode:', mode_count)

#find range

range_of_elements = max_element - min_element

print('Range:', range_of_elements)

#find standard deviation

import statistics

standard_deviation = statistics.stdev(unique_list)

print('Standard deviation:', standard_deviation)

#find variance

variance = statistics.variance(unique_list)

print('Variance:', variance)
