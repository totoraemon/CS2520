#Name : Joseline Ly
#Lab 1 Task 1
#This program will display a user's dream job goal settings

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
company = input("Enter the company you wish to work: ")
salary = float(input("Enter the annual salary you wish to earn in dollars: "))
monthly = salary/12
print("Hello!")

introduction =  'My name is {}, my age is {}' 
print(introduction.format(name, age))
print(f"I hope to work for {company} and earn ${monthly:.2f} a month.")
print()


#Lab 2 Task 2
#This program will request the user to enter an item and amount to return an average price.
product = input("Product: ")
units = int(input("Number of Units Purchased: "))
totalPrice = float(input("Total Price: $"))
avgPrice = totalPrice / units
print(f"Average Price : ${avgPrice:.2f}")

#Output
'''
Please enter your name: Alice Wonderland
Please enter your age: 20
Enter the company you wish to work: Google
Enter the annual salary you wish to earn in dollars: 98576
Hello!
My name is Alice Wonderland, my age is 20
I hope to work for Google and earn $8214.67 a month.

Product: apple
Number of Units Purchased: 3
Total Price: $5
Average Price : $1.67
'''
