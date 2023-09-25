#!/usr/bin/env python3

import os 
import datetime
import emails 
import run
import reports

#------------------------------------------------------------- Process supplier fruit description data
def process_fruit(descriptions):
    open("descriptions_report.txt", 'w').close()

    for k, v in descriptions.items():
        with open("descriptions_report.txt", 'a') as file:
            file.write("name: " + str.capitalize(v['name']) + '\n') 
            file.write("weight: " + str(v['weight']) + "lbs" + '\n')
            file.write('\n\n')

    paragraphs = []
    with open("descriptions_report.txt", 'r') as file:
        for line in file:
            if line.strip():    #Si la línea no está vacía, el código dentro del bloque if se ejecutará
                paragraphs.append(line)  #------------Esto agrega la línea actual a la lista paragraphs
            else:
                paragraphs.append(' ')    #------------Incorpora la línea si está vacía, salto de línea

    return paragraphs

if __name__ == "__main__":

    file_list = os.listdir("supplier-data/descriptions")
    descriptions = run.descriptions_dict(file_list)
    #--------------------------------------------------------------------------------- Generate Report
    title = "Processed Update on " + datetime.datetime.now().strftime("%B %d, %Y")
    paragraph = process_fruit(descriptions)
    reports.generate_report("/tmp/processed.pdf", title, paragraph)

    #-------------------------------------------------------------------------- Send Email with Report
    sender = "automation@example.com"
    receiver = "student-01-be319a71cde8@example.com" 
    subject = "Upload Completed - Online Fruit Store"
    body = "All Fruits are uploaded to our website successfully. A detailed list is attached to this email"

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)


