#Author: Andrew Tkacs

#computer programming

# lab 13-5 Functions

# Function using a dictionary as an argument
def process_data(data_dict):
    result = ""
    for key, value in data_dict.items():
        result += f"{key}: {value}\n"
    return result

#Functions using lists
def manipulate_list(lst):
    return [item * 2 for item in lst]

def analyze_list(lst):
    return sum(lst), max(lst), min(lst)

def modify_list(lst):
    lst.append(10)
    return lst

# Function using a for loop
def iterate_list(lst):
    result = ""
    for item in lst:
        result += str(item) + " "
    return result

# Function using a while loop
def while_loop_example(lst):
    i = 0
    while i < len(lst):
        lst[i] = lst[i] * 10
        i += 1
    return lst

#Function using enumerate
def enumerate_example(lst):
    result = ""
    for index, item in enumerate(lst):
        result += f"Index {index}: {item}\n"
    return result

#Function using builtin functions
def built_in_functions_example(lst):
    return sorted(lst)

#Function getting user input
def get_user_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return f"Hello, {name}! You are {age} years old."

# Function returning
def return_example():
    return "This is a return example."
