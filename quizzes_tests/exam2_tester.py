# Question 1
prices = [10, 20, 30, 40]
for e in prices :
    e *= 1.1
print(prices)

# Question 2
aList = [1,2,3]
cList = [aList*2]
print(cList)

# Question 4
fruit = {"Apple": "Green", "Banana": "Yellow", "Plum": "Purple"}
for k in fruit.values() :  print(k)

# Question 5
data = {"Jan": 31, "Feb": [28, 29], "Mar" : 31}
print(data["Feb"][1])

# Question 6
myName = ("mary", "christmas", "happy", ["holidays", "December"])      # line 1
myName[0] = 'Mary'                                                     # line 2
myName[-1][0]= 'Hoho'                                                  # line 3
print(myName)

# Question 7
animals = ["fish", ("cat", "kitten"), "dog"]   #line 1
animals[1] = "tabby"                           #line 2
print(animals)

# Question 8
tp = (1)
lst = [1, 2]
print(tp[0] + lst(1))

# Question 10
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(values[::-2])

# Question 11
prices = (10, 20, 30, 40)
for x in prices :
    x = x * 1.1
for j in range(len(prices)):
    print(prices[j], end = ", ")
print()
prices = [10, 20, 30, 40]
for j in range(len(prices)) :
    prices[j] = prices[j] *1.1
for x in prices :
    print(x, end = ", ")

# Question 12
def op (dataS, y) :
    dataS[0] = y

L = ['a', 'b', 'c']
op(L, 1)
aTup = ('a', 'b', 'c')
op (aTup, 1)
d = {0: 'a',  2 : 'b'}
op(d, 1)

# Question 13
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)

# Question 15
def f(i):
    try:
        g(i + 5)
    except IndexError:
        print("Index error")

def g(i):
    a = "Hello"
    return a[i]

def main() :
    try:
        f(3)
    except ValueError :
        print("Value Error")
main()