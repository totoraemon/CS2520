# question 26
def task1(word):
    charCount = 0
    for c in word:
        if c.isalpha():
            charCount += 1
    return len(word) - charCount

def task2(n):
    count = 0
    if n < 0:
        return
    elif n == 0:
        return 0
    else:
        for i in range(1, n + 1):
            val = (i ** 2)
            if (i % 2 == 0):
                val *= -1
            count += val
        return count

def main():
    print(f"The result of task1('Hello! How are you?') is {task1("Hello! How are you?")} non-letter characters.") # Task 1 Test 1
    print(f"The result of task1('') is {task1("")} non-letter characters.") # Task 1 Test 2
    print(f"The result of task1('123 let's go!') is {task1("123 let's go!")} non-letter characters.") # Task 1 Test 3
    print(f"The result of task2(10) is {task2(10)}.") # Task 2 Test 1
    print(f"The result of task2(25) is {task2(25)}.") # Task 2 Test 2
    print(f"The result of task2(-1) is {task2(-1)}.") # Task 2 Test 3


main()
'''
Test Run Output:
The result of task1('Hello! How are you?') is 5 non-letter characters.
The result of task1('') is 0 non-letter characters.
The result of task1('123 let's go!') is 7 non-letter characters.
The result of task2(10) is -55.
The result of task2(25) is 325.
The result of task2(-1) is None.
'''