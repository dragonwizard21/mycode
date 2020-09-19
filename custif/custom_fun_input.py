#!/usr/bin/env python3 
""" Wowowowowow

Created by Zach Huff
"""
# imports
import crayons
import csv
# csv file name

def main():
    dev = dev_info()
    print(dev)
    dev_data = {}
    for d in dev:
        dev_data.update({d[0]: d[1:]})
    print(dev_data)
    try:
        usr_input = input("What size is your company? {}, {}, or {}? Choose one.. ".format(crayons.green("Small"), crayons.yellow("Medium"), crayons.red("Large")))
        if usr_input not in ["Small", "Medium", "Large"]:
            raise ValueError
    except ValueError: # If the user doesn't provide the correct input
        print("Oops... Looks like you didn't make a correct selection")
    if usr_input == "Medium":
        print(f"You should use a {dev_data['Medium']} for your company")
        print()
    elif usr_input == "Small":
        print(f"You should use a {dev_data['Small']} for your company")
    else:
        print("You should use a {} for your company".format(crayons.red(' '.join(dev_data['Large']))))


def dev_info():
    filename = "device_info.txt"
    with open(filename, "r", newline='') as f:
        read_csv = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONE)
        head = next(read_csv)
        # Get rid of header
        if head != None:
            data = []
            for row in read_csv:
                print(row)
                data.append(row)
    return data
        #print(read_csv)
        #print(read_csv)
    
main()
