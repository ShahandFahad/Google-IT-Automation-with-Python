"""!/usr/bin/env python """
import sys
import os
import re

"""function error_search that takes log_file as a parameter and returns returned_errors"""


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(
                    error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


"""function file_output that takes returned_errors, returned by a previous function, as a formal parameter."""


def file_output(returned_errors):
    # os.path.expanduser('~') + '/data/
    with open('errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


"""main function and call both functions that we defined in the earlier sections"""
if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)

# sudo chmod +x find_error.py
# TO TEST: ./find_error.py ~/data/fishy.log
# User Input: CRON ERROR Failed to start
