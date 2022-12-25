"""
Question 5
The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.
"""
import os


def parent_directory():
    # Create a relative path to the parent
    c_dir = os.getcwd()
    p_dir_name = os.pardir
    # of the current working directory
    relative_parent = os.path.join(c_dir, p_dir_name)

    # Return the absolute path of the parent directory
    return os.path.realpath(relative_parent)


print(parent_directory())
