#!/usr/bin/env python3

import csv #import the csv module. The csv module provides functionality for working with CSV (Comma-Separated Values) files, which are a common format for storing and manipulating tabular data.


#This function receives a CSV file as a parameter and returns a list of dictionaries from that file
def read_employees(csv_file_location):    
   csv.register_dialect("myDialect", skipinitialspace = True, strict = True)    #myDialect to remove any leading spaces while parsing the CSV file.
   with open(csv_file_location) as file:
      employee_file = csv.DictReader(file, dialect = "myDialect")
      employee_list =[]    #create empty employee list 
      for data in employee_file:
         employee_list.append(data)    #append data into employee list
      return employee_list


#This function receives the list of dictionaries, employee_list as a parameter and return a dictionary of department:amount
def process_data(employee_list):    
   department_list = []    #create empty department_list (list of departments)
   for employee_data in employee_list:
      department_list.append(employee_data["Department"])    #append data into department list
   department_data = {}    #create empty department data dictionary
   for department_name in set(department_list):
      department_data[department_name] = department_list.count(department_name)    #counts how many times each department appear
   return department_data


#This function writes a dictionary of department: amount to a file
def write_report(dictionary, report_file):    
   with open(report_file, "w+") as f:
      for k in sorted(dictionary):    #for each key in the dictionary
         f.write(str(k)+":"+str(dictionary[k])+"\n")    #write the key and the corresponding value as a string
      f.close()


#pass the argument for the function read_employees
employee_list = read_employees("/home/user/data/employees.csv")
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

report_file = write_report(dictionary, "/home/user/report_file.txt")
print(report_file)
