#!/usr/bin/env python3

import re    #import regex module
import csv    #import the csv module

#This function uses regex to identify the domain of the user email addresses in the user_emails.csv file
def contains_domain(address, domain):
  domain_pattern = r'[\w\.-]+@'+domain+'$'    #regex for an email pattern
  if re.match(domain_pattern,address):    
   return True
  return False

#This function takes in one email address at a time, as well as the email's old domain name and its new domain name. Replaces the email addresses containing the old domain name with new domain name.
def replace_domain(address, old_domain, new_domain):
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)    #we use substitution function sub() to replace the old domain name with the new one
  return address

def main():
  old_domain, new_domain = 'abc.edu', 'xyz.edu'    #declare old_domain, new_domain within main
  csv_file_location = '/home/user/data/user_emails.csv'    #store the path of the list user_emails.csv
  report_file = '/home/user/data/updated_user_emails.csv'    #file path for the resulting updated list
  user_email_list = []    #create empty user_email_list
  old_domain_email_list = []    #create empty old_domain_email_list 
  new_domain_email_list = []    #create empty new_domain_email_list

#The data is read from the user_emails.csv file and passed to the user_data_list
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))    
    user_email_list = [data[1].strip() for data in user_data_list[1:]] #This accesses the second element (index 1) of each row, which is assumed to contain the email addresses in the CSV file.
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)    #add the old_domains emails in the old_domain_email_list
        replaced_email = replace_domain(email_address,old_domain,new_domain)    #replace domain
        new_domain_email_list.append(replaced_email)    #add the new_domains emails in the new_domain_email_list
    
    #define the headers for our output file through the user_data_list, which contains all the data read from user_emails.csv file:
    email_key = ' ' + 'Email Address'
        #Line 39, a variable called email_key is being created, which contains the string 'Email Address'. The space before the word "Email" is important because column headers in the CSV file are expected to have a space before the column name. This is later used to identify the column containing the email addresses.
    email_index = user_data_list[0].index(email_key)
        #Line 41 finds the index of the column in user_data_list that contains email addresses. user_data_list[0] represents the first row of data in user_data_list, which is generally assumed to contain the column headers. Then, index(email_key) finds the index of the column whose header matches email_key, which is " Email Address" in this case.

    for user in user_data_list[1:]:    #replace the email addresses within the user_data_list
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == '' + old_domain:
          user[email_index] = '' + new_domain
  f.close()    #Closing the file, although is not necessary in a "with open" block

  with open(report_file, 'w+') as output_file:    #write the report_file
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)    #writing rows with the user_data_list info
    output_file.close()
main()