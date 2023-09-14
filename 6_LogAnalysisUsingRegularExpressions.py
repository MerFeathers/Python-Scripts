#!/usr/bin/env python3
import sys
import re
import csv

#Logs formats:
#info_line = " May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username) "
#error_line = " Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username) "

# Processing logfiles for errors ------------------------------------
error_pattern = r"ticky: ERROR: (.+?) \([\w\.]+\)"
log_files = "log_file.txt"

def error_log_process(log_files):   #---------- Define function -----  
	error_logs = []   #------------------------ Define list of errors

	with open(log_files, mode='r', encoding='UTF-8') as file:
		for log in file.readlines():
			match = re.search(error_pattern, log)
			if match:
				error_message = match.group(1)
			error_logs.append(error_message)
			print(error_logs)   #---------------- Show list of errors
	return error_logs 

# Processing log_files for info and error for usernames --------------
info_pattern = r"ticky: INFO: (.+?) \([\w\.]+\)"

def user_log_process(log_files):   #---------- Define function -------  
	user_logs = {}   #----------------------- Define users dictionary
	
	with open(log_files, mode='r', encoding='UTF-8') as file:
		for log in file.readlines():
			error_match = re.search(error_pattern, log)
			info_match = re.search(info_pattern, log)
			#------------------------- if block for users with errors
			if error_match:
				user = error_match.group(2)
				if user not in user_logs:
					user_logs[user] = {"errors": 1, "info": 0}
				else:
					user_logs[user]["errors"] += 1
			#--------------------------- if block for users with info
			elif info_match:
				user = info_match.group(2)
				if user not in user_logs:
					user_logs[user] = {"errors": 0, "info": 1}
				else:
					user_logs[user]["info"] += 1
					
		print(user_logs)   #------------------- Show users dictionary
		return user_logs


if __name__ == "__main__":   #-------------Define main function -----

#------------------------------------------Defining error_logs in main
	error_logs = error_log_process(log_files)
#	log_files = sys.argv[1]   --------------------use this in the VM!

# Creating error dictionary
	error_dict = {}
	for error in error_logs:
		if error in error_dict:
			error_dict[error] += 1
		else:
			error_dict[error] = 1
		print(error_dict)   #------------------- show errors dictionary

# Sorted dictionary by most common errors
	sorted_error_dict = {k: v for k, v in sorted(error_dict.items(), key=lambda item: item[1], reverse=True)}
	print(sorted_error_dict)   #--------- show sorted errors dictionary

# Create CSV for errors
	with open("error_message.csv", mode="w", newline="", encoding="UTF-8") as error_csv:
		error_writer = csv.writer(error_csv)
		error_writer.writerow(["Error", "Count"])
		for error, count in sorted_error_dict.items():
			error_writer.writerow([error, count])
			
	print("error_message.csv")   #---------------- Show error message CSV

#-----------------------------------------------Defining user_logs in main
	user_logs = user_log_process(log_files)

# Sorted dictionary by username
	sorted_user_logs = {k: v for k, v in sorted(user_logs.items())}
	print(sorted_user_logs)   #------------- Show sorted users dictionary

# Create CSV for users
	with open("user_statistics.csv", mode="w", newline="", encoding="UTF-8") as user_csv:
		user_writer = csv.writer(user_csv)
		user_writer.writerow(["Username", "ERROR", "INFO"])
		for user, stats in sorted_user_logs.items():
			user_writer.writerow([user, stats["errors"], stats["info"]])

	print("user_statistics.csv")   #------------ Show users statistics CSV

