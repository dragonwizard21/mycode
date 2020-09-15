#!/usr/bin/env python3
Computers = ["Dell", "Mac", "HP", "Acer", "Asus"] #list of computer brands
print(Computers)
Addcomputers = ["Microsoft", "Lenovo"]
Computers.extend(Addcomputers) #Add in the computers
#How to add a one off entry?
print(Computers.extend("Ipad"))
