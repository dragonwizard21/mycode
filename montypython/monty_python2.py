#!/usr/bin/env python3
# our counter is called round
round = 0
answer = " "
#Starting our loop
##while True:
#    round = round + 1
#    print("Finish the movie title, 'Monty Python's The Life of ______")
#    answer = input("Your guess here--->  ")
#    if answer == "Brian":
#        print("That's Correct!")
#        break
#    elif round == 3:
#        print("Sorry, the answer was Brian.")
#        break
#    else:
#        print("Sorry, Try again")
while round < 3 and answer != "Brian":
    round += 1 
    answer = input("Finish the movie title, 'Monty Python\'s The Life of _____")
    if answer == "Brian":
        print("Correct")
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else:
        print("Sorry, you are out of guesses. Try again")

