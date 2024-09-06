# Name : Joseline Ly
# Lab 2 Task 1
# This program will allow a user to play rock, paper, scissors against a computer.

while True :
    playerMove = input("Please enter your move (rock, paper, or scissors): ")
    if playerMove == "rock" or playerMove == "paper" or playerMove == "scissors" :
        break
    print(playerMove + " is not a valid move.")


