#!/usr/bin/env python3
# function to push commands
import time
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime)
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to send command --> ' + mycmds)
            # we'll learn to write code that sends cmds to device here

# function for device reboot
"""It should accept a list of IPs as a single argument. The function should iterate through the list IPs, and for each one, print, "Connecting to...,", then print, 'REBOOTING NOW'"""

def devicereboot(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print("Connecting to..," + coffeetime)
        time.sleep(1)
        print("REBOOTING NOW!")

# Start our main script
def main():
    work2do = {"10.1.0.1": ["interface eth1/2", "no shutdown"], "10.2.0.1": 
    ["interface eth1/1", "shutdown"], "10.3.0.1": ["interface eth1/5", "no shutdown"]}
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # Welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

    ## run Second function
    devicereboot(work2do) # call the reboot function

# call our main function 
main()
