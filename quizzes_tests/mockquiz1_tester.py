# Question 1
val = float("12.45")
print(type(val)) # test type of val
print(f"{val}") # test numeric value of val
ans = 13 ** 7.5 
print(f"{ans}") # test numeric value of val

# Question 2
for i in range(-10, 12, 2):
    print(f"{i}")

def checkPrime(num):
    if num <= 1:
        print(f"{num} must be greater than 1.")
    else:
        i = 2
        while i <= num // 2:
            if num % i == 0:
                print(f"{num} is not a prime number.")
                break
            i += 1
        else:
            print(f"{num} is a prime number.")
