"""
Question 2
The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?
"""
import re


def check_time(text):
    pattern = r"^[1-9][0-2]?:[0-5][0-9][ ]?[am|pm]|[AM|PM]$"
    result = re.search(pattern, text)
    # print(result)
    return result != None


print(check_time("12:45pm"))  # True
print(check_time("9:59 AM"))  # True
print(check_time("6:60am"))  # False
print(check_time("five o'clock"))  # False
