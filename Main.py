#############################################
# Name: Ali
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################

# THIS IS WHERE YOU CODE

teams = []

for i in range(1, 7):
name = input(“Team name: “)
wins = int(input(“Wins: “))
ties = int(input(“Ties: “))
losses = int(input(“Losses: “))

points = wins 2 + ties 1

