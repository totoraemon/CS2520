# Name : Joseline Ly
# Project 1 Task 1
# This programs takes a user's present value, a set interest, and the number of years to calculate the future value.
presentValue = float(input("Enter a present dollar amount (float): "))
interest = float(input("Enter an interest amount (float): "))
years = int(input("Enter a number of years (integer): "))
futureValue = presentValue * (1 + interest/100)**years
print(f"The future value is ${futureValue:.2f}")

# Project 1 Task 2
# This programs takes two integers from the user and swaps them, finding the quotient and remainder.
num1 = int(input("Enter an integer for num1: "))
num2 = int(input("Enter an integer for num2: "))
num1, num2 = num2, num1
print(f"The two numbers after swapping are {num1} and {num2}.")
quotient, remainder = num1 / num2, num1 % num2
print(f"The quotient when {num1} / {num2} is {quotient}.")
print(f"The remainder when {num1} is divided by {num2} is {remainder}.")

# Project 1 Task 3
# This programs asks the user to pick a BMI system, their weight and height, and prints their BMI with feedback.
system = input("Please choose a BMI system (English or Metric): ").upper()
if (system == "ENGLISH"):
    weightPounds = int(input("Please enter your weight in lbs (integer): "))
    heightInch = int(input("Please enter your height in inches (integer): "))
    calcBMI = 703 * (weightPounds / (heightInch ** 2))
elif (system == "METRIC"):
    weightKilo = int(input("Please enter your weight in kilograms (integer): "))
    heightMeter = int(input("Please enter your weight in meters (integer): "))
    calcBMI =  weightKilo / (heightMeter ** 2)

if calcBMI < 18:
    print("Your calculated BMI indicates you are underweight.")
elif calcBMI >= 18 and calcBMI <= 25:
    print("Your calculated BMI indicates you are normal.")
else:
    print("Your calculated BMI indicates you are overweight.")