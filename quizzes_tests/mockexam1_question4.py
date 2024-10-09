def testNum(n):
    if n <= 0:
        return 0
    else:
        return 2 * n
    
testNum(-2)
print(f"testNum(-2) returns  {testNum(-2)}") # used to print value and check
testNum(2)
print(f"testNum(2) returns {testNum(2)}") # used to print value and check
testNum(20)
print(f"testNum(20) returns {testNum(20)}") # used to print value and check

'''
Test Runs: 
testNum(-2) returns  0
testNum(2) returns 4
testNum(20) returns 40
'''