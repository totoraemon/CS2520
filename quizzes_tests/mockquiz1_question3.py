def numChar(varWord):
    count = 0
    for character in varWord:
        count += 1
    return count

str = "I have’t started yet, but will do so soon :)"
val = numChar(str)
print(f"There are {val} characters in the string '{str}'")

str = ""
val = numChar(str)
print(f"There are {val} characters in the string '{str}'")

str = "I hope that I can pass this quiz."
val = numChar(str)
print(f"There are {val} characters in the string '{str}'")

'''
Test Runs:
There are 44 characters in the string 'I have’t started yet, but will do so soon :)'
There are 0 characters in the string ''
There are 33 characters in the string 'I hope that I can pass this quiz.'
'''