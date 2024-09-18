# Name : Joseline Ly
# Project 1 Task 1
# This program takes a user's present value, a set interest, and the number of years to calculate the future value.
presentValue = float(input("Enter a present dollar amount (float): "))
interest = float(input("Enter an interest amount (float): "))
years = int(input("Enter a number of years (integer): "))
futureValue = presentValue * (1 + interest/100)**years
print(f"The future value is ${futureValue:.2f}")

'''
Test Run for Task 1:
Enter a present dollar amount (float): 1000.0 
Enter an interest amount (float): 5.0
Enter a number of years (integer): 30
The future value is $4321.94

Enter a present dollar amount (float): 1530.50
Enter an interest amount (float): 3.5
Enter a number of years (integer): 15
The future value is $2564.12

Enter a present dollar amount (float): 5321.07
Enter an interest amount (float): 1.1
Enter a number of years (integer): 100
The future value is $15889.66
'''

# Project 1 Task 2
# This programs takes two integers from the user and swaps them, finding the quotient and remainder.
num1 = int(input("Enter an integer for num1: "))
num2 = int(input("Enter an integer for num2: "))
num1, num2 = num2, num1
print(f"The two numbers after swapping are {num1} and {num2}.")
quotient, remainder = num1 // num2, num1 % num2
print(f"The quotient when {num1} / {num2} is {quotient}.")
print(f"The remainder when {num1} is divided by {num2} is {remainder}.")

'''
Test Run for Task 2:
Enter an integer for num1: 12
Enter an integer for num2: 35
The two numbers after swapping are 35 and 12.
The quotient when 35 / 12 is 2.
The remainder when 35 is divided by 12 is 11.

Enter an integer for num1: 35
Enter an integer for num2: 13
The two numbers after swapping are 13 and 35.
The quotient when 13 / 35 is 0.
The remainder when 13 is divided by 35 is 13.

Enter an integer for num1: 35
Enter an integer for num2: 0
The two numbers after swapping are 0 and 35.
The quotient when 0 / 35 is 0.
The remainder when 0 is divided by 35 is 0.
'''

# Project 1 Task 3
# This programs asks the user to pick a BMI system, their weight and height, and prints their BMI with feedback.
system = input("Please choose a BMI system (English or Metric): ").upper()
weightPounds, heightInch, weightKilo, heightMeter = 0, 0, 0, 0.0
if (system == "ENGLISH"):
    weightPounds = int(input("Please enter your weight in lbs (integer): "))
    heightInch = int(input("Please enter your height in inches (integer): "))
    calcBMI = 703 * (weightPounds / (heightInch ** 2))
elif (system == "METRIC"):
    weightKilo = int(input("Please enter your weight in kilograms (integer): "))
    heightMeter = float(input("Please enter your height in meters (float): "))
    calcBMI =  weightKilo / (heightMeter ** 2)

if weightPounds < 0 or weightKilo < 0:
    print("The weight entered must be an integer greater than 0.")
elif calcBMI < 18:
    print(f"Your calculated BMI is approximately {calcBMI :.2f}.")
    print("This indicates you are underweight.")
elif calcBMI >= 18 and calcBMI <= 25:
    print(f"Your calculated BMI is approximately {calcBMI :.2f}.")
    print("This indicates you are of normal weight.")
else:
    print(f"Your calculated BMI is approximately {calcBMI :.2f}.")
    print("This indicates you are overweight.")

'''
Test Run for Task 3 (Invalid Height):
Please choose a BMI system (English or Metric): English
Please enter your weight in lbs (integer): 120
Please enter your height in inches (integer): 0
ZeroDivisionError: division by zero

Please choose a BMI system (English or Metric): Metric
Please enter your weight in kilograms (integer): 60
Please enter your height in meters (float): 0
Traceback (most recent call last):
ZeroDivisionError: division by zero


Test Run for Task 3 (Negative Weight):
Please choose a BMI system (English or Metric): English
Please enter your weight in lbs (integer): -10
Please enter your height in inches (integer): 70
The weight entered must be an integer greater than 0.

Please choose a BMI system (English or Metric): Metric
Please enter your weight in kilograms (integer): -10
Please enter your height in meters (float): 1.75
The weight entered must be an integer greater than 0.


Test Run for Task 3 (By Case):
Please choose a BMI system (English or Metric): English
Please enter your weight in lbs (integer): 150
Please enter your height in inches (integer): 70
Your calculated BMI is approximately 21.52.
This indicates you are of normal weight.

Please choose a BMI system (English or Metric): English
Please enter your weight in lbs (integer): 200
Please enter your height in inches (integer): 70
Your calculated BMI is approximately 28.69.
This indicates you are overweight.

Please choose a BMI system (English or Metric): English
Please enter your weight in lbs (integer): 100
Please enter your height in inches (integer): 70
Your calculated BMI is approximately 14.35.
This indicates you are underweight.

Please choose a BMI system (English or Metric): Metric
Please enter your weight in kilograms (integer): 68
Please enter your height in meters (float): 1.75
Your calculated BMI is approximately 22.20.
This indicates you are of normal weight.

Please choose a BMI system (English or Metric): Metric
Please enter your weight in kilograms (integer): 85
Please enter your height in meters (float): 1.75
Your calculated BMI is approximately 27.76.
This indicates you are overweight.

Please choose a BMI system (English or Metric): Metric
Please enter your weight in kilograms (integer): 50
Please enter your height in meters (float): 1.75
Your calculated BMI is approximately 16.33.
This indicates you are underweight.

'''