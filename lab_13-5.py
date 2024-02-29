#Author: Andrew Tkacs

#computer Programming

#Lab 13-5

from lab_13-5_functions import process_data, manipulate_list, analyze_list, modify_list

# print 4 functions from the functions file.
data = {'key1': 'value1', 'key2': 'value2'}
print(process_data(data))

lst = [1, 2, 3, 4, 5]
print(manipulate_list(lst))

sum_result, max_result, min_result = analyze_list(lst)
print(f"Sum: {sum_result}, Max: {max_result}, Min: {min_result}")

print(modify_list(lst.copy()))





