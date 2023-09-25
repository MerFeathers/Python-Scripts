#!/usr/bin/env python3

import shutil    
import psutil
import socket
import emails 


#----------------------------------------------------------- Checks if CPU usage is less than 80%, every minute
def check_cpu_usage():
	usage = psutil.cpu_percent(60)
	return usage > 80

#------------------------------------------------------------------------ Checks if free space is more than 20%
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    return percent_free < 20

#--------------------------------------------------------------------- Checks if free memory is more than 500mb
def check_memory_usage():
    memory_stats = psutil.virtual_memory()
    free_memory_mb = memory_stats.available / 2**20
    return free_memory_mb < 500

#--------------------------------------------------------- Checks if a host resolves to the expected IP address
def check_name_resolution(host, expected_ip):
    return socket.gethostbyname(host) != expected_ip


if __name__ == "__main__":
	
    sender = "automation@example.com"
    receiver = "student-01-be319a71cde8@example.com" 
    body = "Please check your system and resolve the issue as soon as possible."

#------------------------------------------------------------- Report an error if CPU usage is over 80%
if check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

#-------------------------------------------- Report an error if available disk space is lower than 20%
if check_disk_usage('/'):
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

#----------------------------------------------- Report an error if available memory is less than 500MB
if check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)

#------------------------- Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
if check_name_resolution('localhost', '127.0.0.1'):
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)
