#Author: Andrew Tkacs

#computer programming

#lab 13-7

# Open the file in read mode
with open('alma-mater.txt', 'r') as file:
    # Read all lines of the file into a list
    lines = file.readlines()

# Print the lines in reverse order with a blank line between each line
for line in reversed(lines):
    print(line.strip())
    print()
