#!/usr/bin/env python3
import uuid # allow us to generate UUID Values

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

for rando in range(howmany): # range is required because an int cannot be looped
    print( uuid.uuid4() )

