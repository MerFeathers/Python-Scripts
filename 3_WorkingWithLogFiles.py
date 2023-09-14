#!/usr/bin/env python3
import sys    #sys module provides information about the Python interpreter's constants, functions, and methods
import os    #os module provides a portable way of using operating system dependent functionality with Python
import re    #We can use regular expressions using re module

#function that takes a user input an search for it in log_file 
def error_search(log_file):
	error = input("What is the error? ")
	returned_errors = []    #create a list with the error log files
	with open(log_file, mode='r',encoding='UTF-8') as file:
		for log in file.readlines():
			error_patterns = ['error']    #create a list to store all the patterns (user input) that will be searched
			for i in range(len(error.split(' '))):
				error_patterns.append(r'{}'.format(error.split(' ')[i].lower()))
				if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):    #to check whether the file has the user defined pattern and, if it is available, append them to the list returned_errors.
					returned_errors.append(log)    
	file.close()
	print(returned_errors)    #For checking***
	return returned_errors    #return the results stored in the list returned_errors


#function that creates an output file errors_found.log
def file_output(returned_errors):
	with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:    #opening the file in writing mode. The method os.path.expanduser ('~'), which returns the home directory of your system instance. concatenate this path (to the home directory) to the file errors_found.log in /data directory
		for error in returned_errors:    #write all the logs to the output file by iterating over returned_errors
			file.write(error)
			print(file_output(returned_errors))    #For checking***
	file.close()
  

#to act as the starting point of execution for any software program. The execution of the program starts only when the main function is defined in Python because the program executes only when it runs directly, and if it is imported as a module, then it will not run

if __name__ == '__main__':    #Define the main function
	log_file = sys.argv[1]    #Defining log_file inside main
	returned_errors = error_search(log_file)    #call to the first function
	file_output(returned_errors)    #call to the second function
	sys.exit(0)    #is used to exit from Python, zero is considered "successful termination"
