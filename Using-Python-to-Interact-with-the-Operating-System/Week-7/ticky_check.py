#!/usr/bin/env python3

# Pakages
import re
import operator
import csv

# Variables and Datastructures
error = {}
per_user = {}
user_name_list = []

# Patterns for differnt REGEX operations
error_pattern = r"(ticky: ERROR) ([\w ']*) \(([\w .]*)\)"
info_pattern = r"(ticky: INFO) ([\w ]*) \[(#[1-9]*)\] \(([\w .]*)\)"

################### Function ##########################
# Count Differnt error and store it in error dictionary


def count_difffernt_errors():
    logfile = open("syslog.log")

    for line in logfile.readlines():
        # Search for error
        error_result = re.search(error_pattern, line)

        if (error_result != None):

            # Count Each Type of Error
            if error_result.group(2) not in error:
                error[error_result.group(2)] = 0
            error[error_result.group(2)] += 1

            # Append user name to list if not int the list
            if error_result.group(3) not in user_name_list:
                user_name_list.append(error_result.group(3))

        # Search for info
        info_result_usr = re.search(info_pattern, line)

        if (info_result_usr != None):
            # Append user name to list if not int the list

            if info_result_usr.group(4) not in user_name_list:
                user_name_list.append(info_result_usr.group(4))

    # Close log file
    logfile.close()

################ FUNCTION END #################


############### FUNCTION #######################
# Count every user info and error and store it in list and return it

def find_error_info(user_name):
    # Serach Error and Info and count it
    logfile2 = open("syslog.log")
    error_counter = 0
    info_counter = 0
    user_error_info_list = []

    for line in logfile2.readlines():
        if user_name in line:

            if (re.search(error_pattern, line)):
                error_counter += 1

            if (re.search(info_pattern, line)):
                info_counter += 1

    # Close log file
    logfile2.close()

    user_error_info_list.append(info_counter)  # Append Info Count
    user_error_info_list.append(error_counter)  # Append Error Count

    return user_error_info_list

################ FUNCTION END #################


################ MAIN #########################

################ **** #########################


# Function Call
count_difffernt_errors()

# Count each user info and error store in per_user dictionary
for user in user_name_list:
    user_error_info_data = find_error_info(user)

    # Assign user error info list to per_user dictionar
    if user not in per_user:
        per_user[user] = user_error_info_data


# SORT using sorted, it will store it in list of tuples so , cast back it to dictionary

# Sort in reverse order the differnt errors dictionary
error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
# Sort per user dictionary by user name
per_user = sorted(per_user.items(), key=operator.itemgetter(0))

# Casting back to dictionary from list of tuples
error = dict(error)
per_user = dict(per_user)


# print(error)
# print(per_user)

###### WRITING to FILES ############
# WRITE TO CSV both dictionaries ###

# File Names
error_csv_file = "error_message.csv"
per_user_csv_file = "user_statistics.csv"

# File Headers

error_csv_file_header = ["Error", "Count"]
per_user_csv_file_header = ["Username", "INFO", "ERROR"]

#####################################
# write error dictionary for csv file

with open(error_csv_file, 'w') as csv_file:
    writer = csv.writer(csv_file)

    # Write header line
    writer.writerow(header_name for header_name in error_csv_file_header)
    # Write data
    for key, value in error.items():
        writer.writerow([key, value])

########################################
# write per_user dictionary to csv file
with open(per_user_csv_file, 'w') as csv_file:
    writer = csv.writer(csv_file)

    # Write header line
    writer.writerow(header_name for header_name in per_user_csv_file_header)
    # Write data, as value is list so we store data through index here
    for key, value in per_user.items():
        writer.writerow([key, value[0], value[1]])
