#!/usr/bin/env python3
#This is a dictionary application
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

##display parts of the dictionary
print( switch["hostname"])
print( switch["ip"])


## request a 'fake' key
#print( switch["lynx"])

## Request a 'fake' key with .get() method
print( "first test = .get()")
print( switch.get("lynx"))

#Other fake key request:
print( "Second test - .get()")
print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!"))

#Third .get() 
print( "Third test - .get()")
print( switch.get("version"))

#Fourth .get() example
print( "Fourth test - .keys()")
print( switch.keys())

#Fifth method
print( "Fifth test - .values.()")
print( switch.values())

#Sixth test
print( "Sixth test - .pop()")
switch.pop("version") #This will remove the version key and associated value pairs
print( switch.keys()) #Version will be gone
print( switch.values()) #The 1.2 value will be gone

#Seventh print example
print( "Seventh test - ADD a new value")
switch["adminlogin"] = "admin123"
print( switch.keys())
print( switch.values())

#Eighth print example
print( "Eigth test - ADD a new value")
switch["password"] = "password123"
print( switch.keys())
print( switch.values())

#Zach test example
print("Ninth test - Add a new value to an existing key")
switch["adminlogin"] = [1, "iceman"]
print( switch.keys())
print( switch.values())


