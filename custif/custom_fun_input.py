#!/usr/bin/env python3 
""" Wowowowowow

Created by Zach Huff
"""
# imports
import crayons
import csv
# csv file name

def main():
    try:
        usr_input = str(input("What size is your company? {}, {}, or {}? Choose one.. ".format(crayons.green("Small"), crayons.yellow("Medium"), crayons.red("Large"))))
    except ValueError: # If the user doesn't provide the correct input
        print("Oops... Looks like you didn't make a correct selection")
    if usr_input == "Medium":
        print("You should use a m{} for your company")
        print()
    elif usr_input == "Small":
        print("You should use a s{} for your company")
    elif usr_input == "Large":
        #print("You should use a {} {} for your company".format(crayons.red(Large())))
   # else:
        pass

# You are going to have to switch some logic here
# We are trying to read in the CSV and have that go through the if/elif/else, not user input
# Alternatively, to achieve your goal...
# I suggest you create a dictionary = {"small": <row data for small>, "medium": ...etc}
# Then you could use that as a key inside of your print function in the logic up above
filename = "device_info.txt"
with open(filename, "r", newline='') as f:
    read_csv = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONE)
    head = next(read_csv)
    # Get rid of header
    if head != None:
    for row in read_csv:
        print(row)
    print(read_csv)
    print(read_csv)




main()
