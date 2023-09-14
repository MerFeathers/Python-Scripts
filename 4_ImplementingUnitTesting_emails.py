#!/usr/bin/env python3
import sys    #sys module provides information about the Python interpreter's constants, functions, and methods
import csv    #import the csv module. The csv module provides functionality for working with CSV

#This function takes the information from a csv file and stores it in a dictionary
def populate_dictionary(filename):
	"""Populate a dictionary with name/email pairs for easy lookup."""
	email_dict = {}    #create empty email dictionary
	with open(filename) as csvfile:
		lines = csv.reader(csvfile, delimiter = ',')    #separate the columns by commas
		for row in lines:
			name = str(row[0].lower())    #name = key for the dictionary = name of the person
			email_dict[name] = row[1]    #email_dict = value for the key in the dictionary = email
	return email_dict

#This function runs in Python and is expected to be called with an argv argument.
def find_email(argv):
	""" Return an email address based on the username given."""
	""" The try blocks (along with except and optionally finally) in Python are used to handle exceptions, that is, exceptional situations or errors that may occur during the execution of a program. Try blocks allow the code to handle these errors in a controlled manner rather than the program crashing or abruptly exiting when an exception occurs."""
	try:    
		fullname = str(argv[1] + " " + argv[2])    #fullname (The argv variable) is used in Python to access the arguments passed to the script when it is run from the command line.
		email_dict = populate_dictionary('/home/username/data/user_mails.csv')    #uses the dictionary from the previous function
		if email_dict.get(fullname.lower()):    #looks up the value associated with the key fullname
			return email_dict.get(fullname.lower())    #If a match is found in the dictionary, this line returns the email address corresponding to the given full name.
		else:
			return "No email address found"    #If no match is found in the dictionary
	except IndexError:
		return "Missing parameters"    #If the user does not provide enough arguments on the command line when running the script the exception is caught and the string "Missing parameters" is returned as a result.

""" Main is a function that takes no arguments and is intended to be the main entry point of your program. 
    In this function you usually put the main code that you want to run when your script runs."""
def main():
	print(find_email(sys.argv))    #This means that the find_email function will be executed with the arguments that were passed to the script when it was run from the command line.

""" This code block checks to see if the script is running directly as a standalone program (that is, not being imported as a module in another script). 
The __name__ variable is a special variable in Python that is set to "__main__" when a script is run directly. Therefore, this line of code ensures that the code in the main function is executed only if the script is running as a main program and not if it is imported as a module in another script."""
if __name__ == "__main__":
	main()