#!/usr/bin/env python3 
import requests

def main():
    """ Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # the .json() method will dump a JSON string into Pythonic data structures.
    # This is much easier than using the urllib.request lib
    print(r.json())

    # Create 3 new lines via the escape character \n
    print("\n\n\n")

    # if we request the 'all' key, we can strip off the outside {}
    # This seems minor, but is CRITICAL if we want to parse our data
    print(r.json().get("all"))

main()
