#!/usr/bin/env python3

#This is my list of games
games = ["WoW", "Star Wars BattleFront", "Star Wars BattleFront II", "Super Smash Bros Melee"]

#These print lines tell you what the first and second entry in my list are
print("The first game in my list is:",  games[0]+"!")
print("And the second is:", games[1]+"!")

#A list of more games
more_games = ["Super Mario Bros", "Zelda", "Halo", "Call of Duty"]

sorted_games = sorted(games + more_games, key=None)

print(sorted_games)

sorted_games.appended("Tetris")
