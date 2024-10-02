# Name : Joseline Ly
# Project 2 Task 1
# This program will have 4 functions.
#
def get_input():
    userString = input("Enter a string: ")
    print(f"{userString} is {len(userString)} characters long.")
    return userString

def get_num_of_letters(word):
    count = 0
    for character in word:
        count += 1
    print(f"{word} has {count} letters.")
    return count

def get_acronym(*words):
    result = ""
    for val in words:
        result += val[0]
    print(f"The acronym for {words} is {result}.")
    return result

def task1():
    get_input()
    get_num_of_letters("woot")
    get_acronym("Random", "Access", "Memory")
    




def main():
    task1()
    #task_2()
    #task_3()

main()