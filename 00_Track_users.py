#!/usr/bin/env python3

import datetime  #----------------------------------- To work with dates and times

#------------------------define helper function to sort the list of events by time
def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)    #----------pass the first function as a key
    machines = {}    #----------------------------- create dictionary for machines
    for event in events:
        try:
            if event.machine not in machines:
                machines[event.machine] = set()    #-----------------------------------------initialize a machine with an empty set for users
            if event.type == "login":
                if event.user in machines[event.machine]:
                    print("{} was already logged in on {}".format(event.user, event.machine))
                else:
                    machines[event.machine].add(event.user)
            elif event.type == "logout":
                if event.user not in machines[event.machine]:
                    print("{} was not logged in on {}".format(event.user, event.machine))
                else:
                    machines[event.machine].remove(event.user)
        except Exception as e:
            print("Error type:", type(e))
            print("Error description:", e)

            #--------------------------------------try block to fix and catch some Errors
    return machines

#--------------------------------------------define function that generates report
def generate_report(machines):
    if not machines:
        print("No active users.")
        return
    
    for machine, users in machines.items():
        if len(users) > 0:    #-------------------------------Ensure that we don't print any machines where nobody is currently logged in
            user_list =", ".join(users)    #------------------The join() function of str gathers the user attributes (which is a string) into a single string, with commas separating the users.
            print("{}: {}".format(machine, user_list))

#---------------------------------------------define class event and its atributes
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

#--------------------------------------------------------define the list of events
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

#-------------------------------------------------------------define main function
def main():
    users = current_users(events)
    print(users)
    generate_report(users)

if __name__ == "__main__":
    main()
