
#author: Andrew Tkacs

# Computer Programming

# Lab_13-2

# I crated a dictionary storing the grades for 6 assignments. (I just made up ranndom numbers for the grades)
grades = {
    "assignment1": 85,
    "assignment2": 92,
    "assignment3": 78,
    "assignment4": 45,
    "assignment5": 24,
    "assignment6": 73
}

# Print a list of just all the grades I received
print(list(grades.values()))

# Print the name of each assignment in the dictionary on a separate line
for assignment in grades.keys():
    print(assignment)

# Print the name and grade I received on each assignment that I scored a 70 or above on.
print("Grades 70 or above:")
for assignment, grade in grades.items():
    if grade >= 70:
        print(f"{assignment}: {grade}")

# Print the name and grade I received on each assignment that I scored a 50 or below on:
print("Grades 50 or below:")
for assignment, grade in grades.items():
    if grade <= 50:
        print(f"{assignment}: {grade}")


#works.
        

