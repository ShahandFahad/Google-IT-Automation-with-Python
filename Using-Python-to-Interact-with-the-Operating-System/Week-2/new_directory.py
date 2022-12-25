"""
Question 2
The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".
"""

import os


def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open(filename, "w") as file:
        pass

    # Return the list of files in the new directory
    c_dir = os.getcwd()
    return os.listdir(c_dir)


print(new_directory("PythonPrograms", "script.py"))
