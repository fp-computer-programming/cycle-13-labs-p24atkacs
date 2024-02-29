#Author: Andrew Tkacs

#computer programming

#lab 13-6

# Open the file with r to read it
with open('alma-mater.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print the line with a blank line after
        print(line.strip())
        print()
