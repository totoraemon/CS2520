# Name : Joseline Ly
# Lab 2 Task 1
# This program will allow a user to play rock, paper, scissors against a computer.
import random
while True:
    # play game at least once
    compMove = random.choice(["rock", "paper", "scissors"])
    while True :
        playerMove = input("Please enter your move (rock, paper, or scissors): ")
        if playerMove == "rock" or playerMove == "paper" or playerMove == "scissors" :
            break
        print(playerMove + " is not a valid move.")

    print("Computer played " + compMove + ".")
    if playerMove == compMove:
        print("It was a tie!")
    elif playerMove == "rock":
        if compMove == "scissors":
            print("You won!")
        else:
            print("Sorry, you lost.")
    elif playerMove == "paper":
        if compMove == "rock":
            print("You won!")
        else:
            print("Sorry, you lost.")
    else:
        if compMove == "paper":
            print("You won!")
        else:
            print("Sorry, you lost.")

    contGame = input("Do you want to play again? (yes or no): ")
    if contGame == "no":
        print("Thank you for playing!")
        break
    else:
        # meant for formatting to differentiate games
        print()

'''
Test Run (demonstrates all test cases and checks for validity of user choice):

Please enter your move (rock, paper, or scissors): rock
Computer played scissors.
You won!
Do you want to play again? (yes or no): yes

Please enter your move (rock, paper, or scissors): paper
Computer played rock.
You won!
Do you want to play again? (yes or no): yes

Please enter your move (rock, paper, or scissors): scissors
Computer played scissors.
It was a tie!
Do you want to play again? (yes or no): yes

Please enter your move (rock, paper, or scissors): scissors
Computer played rock.
Sorry, you lost.
Do you want to play again? (yes or no): yes

Please enter your move (rock, paper, or scissors): clay
clay is not a valid move.
Please enter your move (rock, paper, or scissors): brick
brick is not a valid move.
Please enter your move (rock, paper, or scissors): paper
Computer played rock.
You won!
Do you want to play again? (yes or no): no
Thank you for playing!

'''
