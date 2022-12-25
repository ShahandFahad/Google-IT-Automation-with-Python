"""
Question 2
Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
"""


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km
