# Name : Joseline Ly
# Project 3 Task 1

def task1():

    class Stock():
        """Can create a Stock object with four attributes and has three member functions."""

        def __init__(self, symbol, high, low, closing):
            """initializes a Stock object with its symbol and high, low, and closing prices."""
            self._symbol = symbol
            self._high = float(high)
            self._low = float(low)
            self._closing = float(closing)

        def __str__(self):
            """Overrides the print() function to print out the four variables a Stock object has."""
            return (f"Stock: {self._symbol}\tHigh Price: {self._high}\tLow Price: {self._low}\tClosing Price: {self._closing}")

        def diff(self):
            """Returns the absolute difference between high and low prices."""
            return round(abs(self._high - self._low), 2)
        
        def closing_closest_to_high(self):
            """Returns the absolute difference between closing price and high price."""
            return abs(self._closing - self._high)            

        def high_performance(self):
            """Returns True if closing price is greater than high price."""
            return self._high < self._closing
        

    for i in range(3):
        try:
            filename = input("Please enter a file to be read: ")
            with open(filename, "r") as stocks_file:
                print(f"File {filename} successfully opened.")
                break
        except FileNotFoundError:
            print("File could not be opened.")
            if i == 2:
                print("File could not be opened after 3 attempts. Program terminating.")
                return  # Exit the function gracefully after three failed attempts

    stocks_file = open(filename, "r")
    next(stocks_file)   # Skip the first line of headers

    listStocks = []
    for line in stocks_file:
        listSym = line.split()
        listSym = [item.replace(',', '').strip() for item in listSym]   # Found a "," in one of the values
        if len(listSym) == 4:  # Ensure each line has four values
            stock = Stock(listSym[0], listSym[1], listSym[2], listSym[3])
            listStocks.append(stock)

    # Find the stock with the largest difference between high and low price
    highestDiff = 0
    highestStock = None
    for s in listStocks:
        val = s.diff()
        if val > highestDiff:
            highestDiff = val
            highestStock = s

    if highestStock:
        print(f"Stock with Highest Difference: {highestStock._symbol}")
        print(f"High Price: {highestStock._high}\tLow Price: {highestStock._low}\tDifference: {highestDiff}")\
        
    # Find the stock with closing price closest to the high price
    closestStock = None
    closestDiff = float('inf')  # Start with an infinitely large difference
    for s in listStocks:
        val = s.closing_closest_to_high()
        if val < closestDiff:
            closestDiff = val
            closestStock = s

    if closestStock:
        print(f"Stock with Closest Closing to High Price: {closestStock._symbol}")
        print(f"High Price: {closestStock._high}\tClosing Price: {closestStock._closing}")

    # Print the information for each stock object
    print("\nAll Stocks:")
    for stock in listStocks:
        print(stock)


def task2():
    """Defines class Pair with four methods and main() which tests all methods in Pair."""

    class Pair:
        """Can create a Pair object with x and y values. Overrides print(), +, *, and / operators."""

        def __init__(self, x = 0, y = 0):
            self._x = x
            self._y = y

        def __str__(self):
            return f"<{self._x}, {self._y}>"

        def __add__(self, other):
            return Pair(self._x + other._x, self._y + other._y)
        
        def __mul__(self, other):
            return Pair(self._x * other._x, self._y * other._y)
        
        def __truediv__(self, other):
            return Pair((self._x * self._y - other._x * other._y), (self._x * other._x - self._y * other._y))
        
    def main():
        """Creates three Pair objects and performs mathematical operations."""

        p1 = Pair(3, 2)     # Test __init__ method
        p2 = Pair(1, 5)     # Test __init__ method
        p3 = Pair(4, 3)     # Test __init__ method
        print("Pair 1: ", p1)   # Test __str__ method
        print("Pair 2: ", p2)   # Test __str__ method
        print("Pair 3: ", p3)   # Test __str__ method
        
        print(f"p1 + p2 = {p1 + p2}")   # Test __add__ method
        print(f"p1 * p2 = {p1 * p2}")   # Test __mul__ method
        print(f"p1 / p2 = {p1 / p2}")   # Test __truediv__  method
        print(f"p1 + p2 * p3 = {p1 / p2 * p3}")
        print(f"p1 * p2 / p3 + p1 = {p1 * p2 / p3 + p1}")
        print()     # Used for formatting results

    main()

def task3():
    """Creates Bicycle class and MountainBike class (which extends Bicycle)."""

    class Bicycle:
        """Creates Bicycle object with three member functions. Overrides print() function."""

        def __init__(self, gear, speed):
            self.gear = gear
            self.speed = speed

        def applyBrake(self, decrement):
            self.speed -= decrement
            
        def speedUp(self, increment):
            self.speed += increment

        def addGear(self, numGears):
            """Additional method. Increments self.gear by numGears."""
            self.gear += numGears

        def __str__(self):
            return f"No of gears are {self.gear}\nSpeed of bicycle is {self.speed}"

    class MountainBike(Bicycle):
        def __init__(self, gear, speed, startHeight):
            super().__init__(gear, speed)
            self.seatHeight = startHeight

        def setHeight(self, newValue):
            self.seatHeight = newValue

        def __str__(self):
            return f"{super().__str__()}\nSeat height is {self.seatHeight}"
        
        def speedUp(self, increment):
            """Overrides speedUp() in Bicycle class. Increments self.speed by double the amount."""
            self.speed += increment * 2
        
        def removeGears(self, numGears):
            """Additional method that DOES NOT override any method in Bicycle. Decerements self.gear by numGears."""
            self.gear -= numGears
        
    class Test:
        def main():
            mb = MountainBike(3, 100, 25)
            print(mb)
            print()     # Used for formatting results

            mb.setHeight(20)
            mb.speedUp(25)
            mb.removeGears(1)
            print(mb)
            print()     # Used for formatting results

            b = Bicycle(3, 100)
            print(b)
            print()     # Used for formatting results

            b.speedUp(25)
            b.addGear(1)
            print(b)
            print()     # Used for formatting results
            b.applyBrake(10)
            print(b)
            print()     # Used for formatting results

        main()

def main():
    task1()
    print("End of task1()\n")
    task2()
    print("End of task2()\n")
    task3()
    print("End of task3()\n")

main()
"""
Please enter a file to be read: symbols.txt
File symbols.txt successfully opened.
Stock with Highest Difference: META
High Price: 531.5       Low Price: 518.15       Difference: 13.35
Stock with Closest Closing to High Price: AMD
High Price: 141.19      Closing Price: 141.13

All Stocks:
Stock: AAPL     High Price: 221.89      Low Price: 219.01       Closing Price: 221.27
Stock: AMD      High Price: 141.19      Low Price: 137.52       Closing Price: 141.13
Stock: AMZN     High Price: 171.04      Low Price: 167.1        Closing Price: 170.23
Stock: GME      High Price: 22.38       Low Price: 21.86        Closing Price: 22.27
Stock: GOOG     High Price: 165.93      Low Price: 166.54       Closing Price: 164.77
Stock: INTC     High Price: 20.47       Low Price: 20.48        Closing Price: 19.47
Stock: LOGI     High Price: 88.2        Low Price: 86.63        Closing Price: 87.76
Stock: META     High Price: 531.5       Low Price: 518.15       Closing Price: 528.54
Stock: MSFT     High Price: 414.95      Low Price: 409.57       Closing Price: 414.01
Stock: NVDA     High Price: 116.23      Low Price: 111.58       Closing Price: 116.14
Stock: SONY     High Price: 89.16       Low Price: 87.37        Closing Price: 89.06
Stock: TSLA     High Price: 208.49      Low Price: 197.06       Closing Price: 207.83
End of task1()

Pair 1:  <3, 2>
Pair 2:  <1, 5>
Pair 3:  <4, 3>
p1 + p2 = <4, 7>
p1 * p2 = <3, 10>
p1 / p2 = <1, -7>
p1 + p2 * p3 = <4, -21>
p1 * p2 / p3 + p1 = <21, -16>

End of task2()

No of gears are 3
Speed of bicycle is 100
Seat height is 25

No of gears are 2
Speed of bicycle is 150
Seat height is 20

No of gears are 3
Speed of bicycle is 100

No of gears are 4
Speed of bicycle is 125

No of gears are 4
Speed of bicycle is 115

End of task3()
"""
