"""
Question 1
The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".
"""
import os


def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "a+") as pyFile:
        pyFile.write(comments)
        print(pyFile.read())
        filesize = os.path.getsize(filename)

    return (filesize)


print(create_python_script("program.py"))
