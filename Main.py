#############################################
# Name: Ali
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE
print("Enter the team name?")
name = input("team name: ")
wins = int(input("wins: "))
ties = int(input("ties: "))
losses = int(input("losses: "))
points = (wins * 2)+(ties * 1)
summary = f" team name: {name} wins: {wins} ties: {ties} losses: {losses} points: {points}
print(summary)
