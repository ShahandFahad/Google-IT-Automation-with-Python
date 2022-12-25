"""
Question 3
Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.
"""


def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n > 0):
        count += 1
        n = int(n / 10)
    return count


print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))    # Should print 1
