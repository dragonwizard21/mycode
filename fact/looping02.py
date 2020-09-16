#!/usr/bin/env python3
# open file in read mode
dnsfile = open("dnsserver.txt", "r") # open() with read mode which equals  "r"? Also would you have to type the whole path of a file if it was sitting somewhere else in the FS?
dnslist = dnsfile.readlines()

for svr in dnslist:
    print(svr, end=" ") # print and end without a new line

