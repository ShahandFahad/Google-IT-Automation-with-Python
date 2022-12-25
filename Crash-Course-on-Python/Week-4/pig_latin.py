"""
Question 2
Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay."""


def pig_latin(text):
    say = ""
    # Separate the text into words
    list = []
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say = word[1:] + word[:1] + "ay"
        list.append(say)
        # Turn the list back into a phrase
    return ' '.join(list)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))
