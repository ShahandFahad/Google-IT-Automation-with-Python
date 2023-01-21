#!/usr/bin/env python3
"""
Imagine one of your IT coworkers just retired and left a folder of scripts for you to use. One of the scripts, called emails.py, matches users to an email address and lets us easily look them up! For the most part, the script works great — you enter in an employee's name and their email is printed to the screen. But, for some employees, the output doesn't look quite right. Your job is to add a test to reproduce the bug, make the necessary corrections, and verify that all the tests pass to make sure the script works! Best of luck!
"""
import csv
import sys


def populate_dictionary(filename):
    user_emails = {}
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        is_head = True
        for name, email in csv_reader:
            if is_head:
                is_head = False
                continue
            else:
                user_emails[name] = email

    return user_emails


def find_email(argv):
    user_emails = populate_dictionary('user_emails.csv')
    # if (len(argv) < 3):
    #     return "Missing parameters"
    try:
        user_name = argv[1] + " " + argv[2]
    except:
        return "Missing parameters"
    if user_name not in user_emails:
        return "No email address found"
    if user_name in user_emails:
        # print(user_emails[user_name])
        return user_emails[user_name].strip()


# find_email("Blossom Gill")
# find_email("Oren Rollins")

# user_name = sys.argv[1] + " " + sys.argv[2]
