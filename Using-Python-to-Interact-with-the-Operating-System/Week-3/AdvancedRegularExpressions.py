# Question

"""
Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames.
"""
import re


def rearrange_name(name):
    # can be done like this
    # r"^(\w*), (\w*) ([A-Z].)$"
    # "{} {} {}".format(result[2], result[3], result[1]
    #  "^([\w \.-]*), ([\w \.-]*)$"
    # Can be done like this
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)

# Question

"""
The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.
"""


def long_words(text):
    pattern = r"\w{7,}"
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
# ['chocolate', 'afternoon']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
print(long_words("I never drink tea late at night."))  # []

# Question

"""
Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
"""


def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]*)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


# 12345 (ERROR)
print(extract_pid(
    "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid(
    "A string that also has numbers [34567] but no uppercase message"))  # None
# 67890 (RUNNING)
print(extract_pid(
    "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))
