# Name : Joseline Ly
# Lab 3 Task 1
# This program will create a cherry blossom tree generated with the turtle module.
# Source: 

from turtle import * # import turtle module
import turtle
from time import sleep 
import random

# tree(branchLen) is a recursive function used to create the branches of the tree
def tree(branchLen):
    if branchLen > 3:
        if 8 <= branchLen <= 12:
            if random.randint(0,2) == 0: # allows petals to vary between the colors "snow" and "lightcoral"
                color('snow')
            else:
                color('lightcoral')
            pensize(branchLen / 3) # changing pensize allows for varying branch sizes
        elif branchLen < 8:
            if random.randint(0,1) == 0:
                color('snow')
            else:
                color('lightcoral')
            pensize(branchLen / 2)
        else:
            color('sienna') # creates the actual branch that petals sit on
            pensize(branchLen / 10)

        forward(branchLen)
        a = 1.5 * random.random()
        right(20 * a)
        b = 1.5 * random.random()
        tree(branchLen - 10 * b)
        left(40 * a)
        tree(branchLen - 10 * b)
        right(20 * a)
        up()
        backward(branchLen)
        down()

# petal(n) creates loose petals that pool underneath the tree
def petal(n):
    for i in range(n):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        up()
        forward(b)
        left(90)
        forward(a)
        down()
        color('lightcoral')
        circle(1)
        up()
        backward(a)
        right(90)
        backward(b)

def ground():
    up()
    color('green')
    

def main():
    turtle.setup(500, 750, 0, 0)
    tracer(0, -100) # changed starting position
    bgcolor('LightBlue') # sets the background of the window to "LightBlue"
    left(90)
    up()
    backward(50)
    down()
    color('sienna')
    tree(60) # builds a tree, use of random generates different tree each run
    petal(100) # generates petals at base of tree
    ht()

    exitonclick()

main()