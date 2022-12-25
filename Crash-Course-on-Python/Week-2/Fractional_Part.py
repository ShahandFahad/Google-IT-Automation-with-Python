"""
Question 10
The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.
"""


def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    if (denominator == 0):
        return 0
    else:
        fractional_part = float(numerator / denominator)
        fractional_part = fractional_part - int(fractional_part)
        return fractional_part
# keep just the fractional part of the quotient
    return 0


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0
