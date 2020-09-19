#!/usr/bin/env python3
import requests

def main():
    """ run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # this is much easier than using the urllib.request lib
    print(r.json())
main()
