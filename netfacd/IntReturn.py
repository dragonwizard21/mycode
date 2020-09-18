#!/usr/bin/env python3
import netifaces

# Create a function that returns just the IP address when passed an adpater name
print(netifaces.interfaces())
user_selected_int = input("Please make a interface selection." + str(netifaces.interfaces()) + "Which one?")
#
# Create a function that returns just the MAC address when passed an adapter name


