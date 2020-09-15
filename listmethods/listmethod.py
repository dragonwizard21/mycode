#!/usr/bin/env python3
#protocols the user uses:
protocol = ["ssh", "http", "https"]
#Asks the user what protocol they are using.
userprot = raw_input("What protocol are you using?  " + protocol[0] + protocol[1] + protocol[2], \n "Please select one..")
print("This is your current protocol:" + protocol[0])
print(protocol)
