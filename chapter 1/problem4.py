# write a program to print the contents of a directory using the os module.
# search online for the function which does that.(chat gpt)
import os

# Specify the directory path
directory_path = "."

# Get and print the contents of the directory
contents = os.listdir(directory_path)

for item in contents:
    print(item)