"""
Question 4
This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column). Fill in the blanks so that calling multiplication_table(1, 3) will print out:

1 2 3 

2 4 6 

3 6 9
"""


def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(1, stop+1):
            print(str(x*y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above
