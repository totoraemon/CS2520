# Name : Joseline Ly
# Lab 4 Task 1
import time     # used in task1() and task2()
import random   # used in task2() and task3()

def task1():
    """
    This program will display the execution time of creating a list of 10 elements with values entered by user.
    This function includes the time it takes the user to input their values as creating such a small list takes close to 0 seconds.
    If this function were to exclude the time for user input, the execution time would be 0.000000 seconds.
    """ 
    start_time = time.time()

    values = []
    line = input("Enter 10 integers: ")
    line = line.split()

    if len(line) != 10: # ensures the line holds exactly 10 values
        print("Error: You must enter exactly 10 integers.")
    else:
        for val in line:
            values.append(int(val))  # converts each value to an integer

    end_time = time.time()
    print(f"Values: {values}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")

# Lab 4 Task 2
def task2(size):
    "This program will display the execution times of generating two lists with random integers of different sizes."
    print(f"Size = {size}")

    L1 = []
    start1 = time.time()
    for i in range(size):
        L1.append(random.randint(1,100))
    end1 = time.time()
    exec1 = end1 - start1 # calculates execution time for method 1
    print(f"Values (Method 1): {L1}") # commented out during test runs 2 - 4
    print(f"Execution Time (Method 1) = {exec1:.6f} seconds")

    start2 = time.time()
    L2 = [random.randint(1,100) for val in range(size)]
    end2 = time.time()
    exec2 = end2 - start2 # calculates execution time for method 2
    print(f"Values (Method 2): {L2}") # commented out during test runs 2 - 4
    print(f"Execution Time (Method 2) = {exec2:.6f} seconds")

# Lab 4 Task 3
def task3():
    "This program generates a list of length 500 in 6 different ways."
    L1 = []
    for i in range(500):
        val = 1
        while val % 2 != 0:
            val = random.randint(1,100)
        L1.append(val)

    L2 = [random.choice(range(2, 101, 2)) for val in range(500)]

    L3 = []

    print(L1)
    print(L2)
    print(L3)
    print(L4)
    print(L5)
    print(L6)



def main():
    # task1()       # Task 1 Test 1 with values 1 2 3 4 5 6 7 8 9 10
    # task1()       # Task 1 Test 2 with values 2 4 6 8 10 12 14 16 18 20
    # task1()       # Task 1 Test 3 with values 10 20 30 40 50 60 70 80 90 100
    # task2(50)       # Task 2 Test 1 with size = 50
    # task2(500)      # Task 2 Test 2 with size = 500
    # task2(5000)     # Task 2 Test 3 with size = 5000
    # task2(50000)    # Task 2 Test 4 with size = 50000
    task3()

main()
'''
Test Runs for Task 1:
Enter 10 integers: 1 2 3 4 5 6 7 8 9 10
Values: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Execution time: 10.437774 seconds

Enter 10 integers: 2 4 6 8 10 12 14 16 18 20 
Values: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Execution time: 9.222470 seconds

Enter 10 integers: 10 20 30 40 50 60 70 80 90 100
Values: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Execution time: 9.124076 seconds


Test Runs for Task 2:
Size = 50
Values (Method 1): [55, 98, 24, 97, 62, 73, 36, 77, 43, 4, 36, 40, 69, 58, 75, 51, 24, 31, 72, 81, 38, 72, 10, 96, 62, 61, 88, 2, 79, 32, 21, 99, 100, 61, 17, 24, 59, 46, 76, 13, 95, 28, 57, 77, 62, 87, 59, 24, 9, 88]
Execution Time (Method 1) = 0.000000 seconds
Values (Method 2): [73, 42, 11, 25, 67, 1, 20, 52, 97, 65, 50, 4, 60, 71, 43, 28, 47, 36, 59, 50, 69, 15, 58, 4, 69, 35, 54, 14, 8, 70, 49, 46, 62, 73, 42, 39, 85, 95, 53, 78, 31, 67, 10, 48, 70, 50, 1, 55, 88, 81]
Execution Time (Method 2) = 0.000000 seconds

(For test runs 2 - 4, I chose not to print or provide the array of values as their sizes are large.)
Size = 500
Execution Time (Method 1) = 0.000000 seconds
Execution Time (Method 2) = 0.000000 seconds
Size = 5000
Execution Time (Method 1) = 0.000000 seconds
Execution Time (Method 2) = 0.010285 seconds
Size = 50000
Execution Time (Method 1) = 0.049502 seconds
Execution Time (Method 2) = 0.047196 seconds
'''