
import csv
#!/usr/bin/env python3

"""
Introduction
For this lab, imagine you are an IT Specialist at a medium-sized company. The Human Resources Department at your company wants you to find out how many people are in each department. You need to write a Python script that reads a CSV file containing a list of the employees in the organization, counts how many people are in each department, and then generates a report using this information. The output of this script will be a plain text file."""

"""
1. Convert employee data to dictionary
The goal of the script is to read the CSV file and generate a report with the total number of people in each department. To achieve this, we will divide the script into three functions.

Let's start with the first function: read_employees(). This function receives a CSV file as a parameter and returns a list of dictionaries from that file. For this, we will use the CSV module.

"""


def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(
        open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list


# Testing function rea_employees
employee_list = read_employees(
    'employees.csv')
# print(employee_list)

"""
2. Process employee data
The second function process_data() should now receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount.
"""
# Return redundant department data in form of dictionary


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name
                        ] = department_list.count(department_name)

    return department_data


# Test it
dictionary = process_data(employee_list)
# print(dictionary)

"""
3. Generate a report
Next, we will write the function write_report. This function writes a dictionary of department: amount to a file.

The report should have the format:

<department1>: <amount1>

<department2>: <amount2>
"""

# Generate Report of the data


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()


# call the function
write_report(dictionary, 'test_report.txt')
