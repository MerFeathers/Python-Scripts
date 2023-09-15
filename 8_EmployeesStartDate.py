#!/usr/bin/env python3

import datetime    #module for working with dates
import requests    #module for making HTTP requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

#Interactively prompts the user to input a start date for querying employee data.
def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

#Downloads a file from the specified URL and returns its contents as a dictionary
def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    response = requests.get(url, stream=True)    #------------------------------------Downloads the file from the url

    lines = []    #-------------------------------------------------------------------Initializes an empty list called lines, this list will be used to store the individual lines of the CSV file retrieved from the URL
    data = {}    #--------------------------------------------------------------------Initializes an empty dictionary called data. This dictionary will be used to store the processed data extracted from the CSV file
    for line in response.iter_lines():    #-------------------------------------------Iterates through the lines of the CSV file, which are obtained by iterating through the streamed response from the URL
        lines.append(line.decode("UTF-8"))    #---------------------------------------Each line from the response is decoded from bytes to a string using UTF-8 encoding and then appended to the lines list.
    for user in lines:
        user = user.split(",")
        name = user[0] + " " + user[1]    #-------------------------------------------This line constructs a full name for the user by concatenating the first and second elements of the user list
        date = user[3]    #-----------------------------------------------------------This line extracts the date of employment
        data.update({name: date})    #------------------------------------------------Adds an entry to the data dictionary where the key is the user's full name (name) and the value is the user's date of employment (date)
    data.pop("Name Surname")    #-----------------------------------------------------Removes an entry from the data dictionary with the key "Name Surname." This is done to eliminate any header present in the CSV file.
    print(data)
    return data
    
#This function takes a start date and the employee data dictionary. It finds employees who started on the provided date or the closest newer date by iterating through the data and comparing dates
#We want all employees that started at the same date or the closest newer date. To calculate that, we go through all the data and find the employees that started on the smallest date that's equal or bigger than the given start date.
def get_same_or_newer(start_date, data):
    min_date = datetime.datetime.today()    #------------------------------------------Itializes a variable called min_date with the current date and time obtained using datetime.datetime.today()
    min_date_employees = []    #-------------------------------------------------------Initializes an empty list called min_date_employees
    for user, date in data.items():
        row_date = datetime.datetime.strptime(date, '%Y-%m-%d')    #-------------------It converts the start date (which is a string in the format 'YYYY-MM-DD') into a datetime object and assigns it to the variable row_date. This allows for date comparison.
        if row_date < start_date:    #-------------------------------------------------If this date is smaller than the one we're looking for, we skip this row
            continue
        if row_date < min_date:    #---------------------------------------------------This if statement checks if the row_date is smaller (earlier) than the current min_date. If it is, it updates min_date to be the row_date and resets the min_date_employees list to an empty list. This is done to start a new list of employees for the new minimum date.
            min_date = row_date
            min_date_employees = []
        if row_date == min_date:    #---------------------------------------------------This if statement checks if the row_date is equal to the current min_date. If they are the same, it appends the name of the employee (formatted as a string) to the min_date_employees list.
            min_date_employees.append("{}".format(user))

    return min_date, min_date_employees

#Function that takes two arguments: start_date (a date to start the list from) and data (a dictionary containing employee names as keys and start dates as values).
def list_newer(start_date, data):
    while start_date < datetime.datetime.today():    #----------------------------------This line starts a while loop that continues as long as the start_date is less than the current date and time, obtained using datetime.datetime.today(). This loop is used to iterate through dates, starting from start_date and moving forward until reaching the current date.
        start_date, employees = get_same_or_newer(start_date, data)    #----------------It retrieves the minimum date and a list of employees who started on that date or the closest newer date, and assigns them to the variables start_date and employees.
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)    #-----------------------This line increments the start_date by one day using datetime.timedelta(days=1). This is done to move to the next date in the loop and continue the iteration.


#Function that orchestrates the entire process. It gets the user's start date choice, loads employee data, and lists employees based on the chosen start date.
def main():
    """Returns the employees that started on given date, or the closet one"""
    data = get_file_lines(FILE_URL)
    start_date = get_start_date()
    list_newer(start_date, data)

if __name__ == "__main__":    #----------------------------------------------------------The script's execution is controlled by this block, which ensures that the main() function is called when the script is run directly.
    main()