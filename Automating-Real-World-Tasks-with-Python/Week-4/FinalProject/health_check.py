#!/usr/bin/env python3
import psutil
import shutil
import socket
import emails
import time
import os

"""
    Report an error if CPU usage is over 80%
    Report an error if available disk space is lower than 20%
    Report an error if available memory is less than 500MB
    Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""
# Return cpu usage
def cpu_usage(duration):
    return psutil.cpu_percent(duration)

# Return Disk Space
def disk_space(path):
    stat = shutil.disk_usage(path)
    return (stat.free/stat.total * 100)

# Return Avaialable Memory in MB
def available_memory():
    avaialble_memory = psutil.virtual_memory()
    return (avaialble_memory.available / 1024)

# Return Host
def get_host_name():
    socket_name = socket.gethostname()
    return socket.gethostbyname(socket_name)

# Check overall system statistics
def check_system_statistics(duration):
    sender = "automation@example.com"
    recipient = "student-01-d065d0029399@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    
    localhost = "127.0.0.1"
    path = os.getcwd()
    
    max_cpu_usage = 80
    minimum_disk_space = 20
    minimum_available_memory = 500
    
    if(cpu_usage(duration) > max_cpu_usage):
        subject = "Error - CPU usage is over 80%"
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)
    elif(disk_space(path) < minimum_disk_space):
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)
    elif(available_memory() < minimum_available_memory):
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate_error_report(sender, recipient, subject, body)
        emails.send_email(message)
    elif(localhost != get_host_name()):
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate_error_report(sender, recipient, subject, body)
        print(message)
        emails.send_email(message)
        print(subject)
        
    else:
        print("NO issue")
        
    time.sleep(duration)




if __name__ == '__main__':
    duration = 60 # 60 seconds
    while True:
     check_system_statistics(duration)