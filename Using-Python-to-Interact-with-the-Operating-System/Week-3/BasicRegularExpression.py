import re
# ----------------------------
# Basic Regular Expressions
# Week 3
# Module 2 Videos Short Quizes
# -----------------------------
# Question: Simple Matching in Python
"""
Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
"""


def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True
# Question: Wildcards and Character Classes
"""
Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.
"""


def check_punctuation(text):
    result = re.search(r"[,.?:;?!]", text)
    return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False
# Question: Repetition Qualifiers
"""
The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work. 
"""


def repeating_letter_a(text):
    result = re.search(r"[aA].*[aA]", text)
    return result != None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True
# Question: Escaping Characters
"""
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.
"""


def check_character_groups(text):
    result = re.search(r"\d", text)
    return result != None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

# Question: Regular Expressions in Action
"""
Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
"""


def check_sentence(text):
    result = re.search(r"^[A-Z][a-z0-9 -]*[.?!]$", text)
    return result != None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True
