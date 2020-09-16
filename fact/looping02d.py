#!/usr/bin/env python3

with open("dnsserver.txt", "r") as dnsfile: # open file in read mode
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char if exists

        if svr.endswith('org'): # if string for svr ending with 'org'
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")
        elif svr.endswith('com'): # elif string for svr ending with 'com'
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")

# no need to close our file - closed automatically 
