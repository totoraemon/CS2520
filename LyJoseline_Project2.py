# Name : Joseline Ly
import array # used for task2()

# Project 2 Task 1
# This program consists of 3 functions: get_input(), get_num_of_letters(word), and get_acronym(*words).
# get_input() takes a string from the user and returns its length.
def get_input():
    userString = input("Enter a string: ")
    print(f"{userString} is {len(userString)} characters long.\n")
    return userString

# get_num_of_letters(word) takes a string for the argument and prints how many letters are in the argument.
def get_num_of_letters(word):
    count = 0
    for character in word:
        count += 1
    print(f"{word} has {count} letters.\n")
    return count

# get_acronym(*words) takes in a variable amount of strings and returns the first character of each to print out an acronym.
def get_acronym(*words):
    result = ""
    for val in words:
        result += val[0]
    print(f"The acronym for {words} is {result}.\n")
    return result

# task1() runs 2 test cases for get_input(), get_num_of_letters(word), and get_acronym(*words)
def task1():
    get_input()
    get_num_of_letters("apple")
    get_acronym("Random", "Access", "Memory")
    get_input()
    get_num_of_letters("orange")
    get_acronym("American", "Airlines")

# task2 
def task2(): 
    val = 0
    prime = []
    while True:
        if (is_prime(val)):
            prime.append(val)
        val += 1

def is_prime(x):
    if x > 1:
        for i in range(2, (x//2)+1):
            if (x % i == 0):
                return False
                break
        else:
            return True
    else:
        return False

def first_50_prime():
    primeNums = []
    num = 0
    while len(primeNums) < 50:
        if (is_prime(num)):
            primeNums.append(num)
        num += 1
    
    # prints out 10 prime numbers per line
    for n in primeNums:
        if ((primeNums.index(n)  + 1) % 10 == 0):
                print(f"{n}\n")
        else:
            print(n, end = " ")

def task3():
    return 1
    


def main():
    #task1()
    #first_50_prime()
    task2()
    #task_3()

main()

'''
Test Run for task1():
Enter a string: happy
happy is 5 characters long.

apple has 5 letters.

The acronym for ('Random', 'Access', 'Memory') is RAM.

Enter a string: upset
upset is 5 characters long.

orange has 6 letters.

The acronym for ('American', 'Airlines') is AA.
'''