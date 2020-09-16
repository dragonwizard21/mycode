#!/usr/bin/env python3
"""This is Zach Huff's custom if script!"""
message = "The movie is about to begin, we recommend "

#wrap connection in a float() to accept decimals as numbers
connection = float(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 25:
    message = message + "Setting video to 4k"
elif connection >=5:
    message = message + "Setting video to 1080p"
elif connection >=2:
    message = message + "Buffering.. slow internet speeds"
else:
    message == "404 site not found"
print(message)
