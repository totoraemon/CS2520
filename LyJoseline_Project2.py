# Name : Joseline Ly
import array # used for task2()

# Project 2 Task 1
# This program consists of 3 functions: get_input(), get_num_of_letters(word), and get_acronym(*words).
def get_input():
    "get_input() takes a string from the user and returns its length"
    userString = input("Enter a string: ")
    print(f"{userString} is {len(userString)} characters long.")
    return userString

def get_num_of_letters(word):
    "get_num_of_letters(word) takes a string for the argument and prints how many letters are in the argument"
    count = 0
    for character in word:
        count += 1
    print(f"{word} has {count} letters.")
    return count

def get_acronym(*words):
    "get_acronym(*words) takes in a variable amount of strings and returns the first character of each to print out an acronym"
    result = ""
    for val in words:
        result += val[0]
    print(f"The acronym for {words} is {result}.\n")
    return result


def task1():
    "task1() runs 3 test cases for get_input(), get_num_of_letters(word), and get_acronym(*words)"
    get_input()
    get_num_of_letters("apple")
    get_acronym("Random", "Access", "Memory")
    get_input()
    get_num_of_letters("orange")
    get_acronym("American", "Airlines")
    get_input()
    get_num_of_letters("banana")
    get_acronym("Central", "Processing", "Unit")

def is_prime(x):
    "is_prime(x) takes an integer x and returns True if it is prime and False otherwise"
    if x > 1:
        for i in range(2, (x//2)+1):
            if (x % i == 0):
                return False
                break
        else:
            return True
    else:
        return False

def prime_generator():
    "prime_generator() yields integer n if it is prime"
    n = 2
    while True:
        if is_prime(n): 
            yield(n)
        n += 1

# Project 2 Task 2
# This program uses prime_generator() generate prime values and yield them. 
def task2():
    """
    task2() uses prime_generator() to print the first 50 prime numbers, skip the next 10 prime numbers, print the following 
    10 prime numbers, then print the count of prime numbers from the 70th (exclusive) until the value 5000
    """
# next 10 prime numbers"
    primeNums = []
    p = prime_generator()
    # adds values given by prime_generator() until primeNums has a size of 50
    for i in range(50):
        primeNums.append(next(p))
    # skips the next 10 values (or indices 51 - 60)
    for i in range(10):
       next(p)
    # added the next 10 values (or indices 61 - 70) after skipping
    for i in range(10):
        primeNums.append(next(p))

    # creates a new array to count the the amount of prime numbers between the 70th and the value 5000
    primeAfter70 = []
    val = next(p)
    while val < 5000:
        primeAfter70.append(val)
        val = next(p)
    count = len(primeAfter70)

    # prints out 10 prime numbers per line
    for i in range(len(primeNums)):
        if (i + 1) % 10 == 0:
            print(primeNums[i])
        else:
            print(primeNums[i], end=" ")

    # prints out how many prime numbers exist between the 70th prime number and the value 5000
    print(f"After the 70th prime number, there are {count} prime numbers between {primeNums[len(primeNums) - 1] + 1} and 5000.")

def main():
    "main() calls task1() and task2()"
    task1()
    task2()

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

Enter a string: excited
excited is 7 characters long.
banana has 6 letters.
The acronym for ('Central', 'Processing', 'Unit') is CPU.

Test Run for task2():
2 3 5 7 11 13 17 19 23 29
31 37 41 43 47 53 59 61 67 71
73 79 83 89 97 101 103 107 109 113
127 131 137 139 149 151 157 163 167 173
179 181 191 193 197 199 211 223 227 229
283 293 307 311 313 317 331 337 347 349
After the 70th prime number, there are 599 prime numbers between 350 and 5000.
'''