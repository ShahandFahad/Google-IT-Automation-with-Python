##!/usr/bin/env python3

def character_frequency(filename):
    """Counts the frequency of each character in given file"""

    # First try to open the file
    try:
        f = open(filename)
    except:
        return None

    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close
    return characters


frequency = character_frequency("Reading.txt")
print(frequency)
