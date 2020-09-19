#!/usr/bin/env python3
import requests

def main():
    """ Run time code"""
    # crate r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # display the method available to our new object
    print( dir(r) )
main()
