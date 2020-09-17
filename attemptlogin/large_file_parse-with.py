#!/usr/bin/env python3
loginfail = 0 # This is the counter for fails

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "-----] Authorization failed" in line:
            loginfail += 1 # This is the same as loginfail = loginfail + 1
print("The number of failed log in attempts is", loginfail)
