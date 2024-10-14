
# question 2
x = "wow"
y = "hi"
z = "bye"
print(x>y<z)

# question 3
words = "JavaPython"
wrd = words[1::2]
print(wrd)

# question 8
# CHECK
i, seed = 0, 1
while i != seed :
    i=i+2
    if i > 20 :
        break
else:
    print('Haha')

# question 10
def fun (x) :
      print(x*2)     #first line of print 
result = fun(5)
print(result)        #second line of print

# question 11
def f (x) :
     return g(x+2)  
def g (y) :
     if y > 10 :
        return y
     else :
        return f(y)
num = 5
print(f(num))

# question 16
def g() :
    num = 1 #initialize num with 1
    while True :
        num += 1 #num increased by 1
        yield num
my_g = g()
for j in range(5):
    result = next(my_g)
    print(result) #here we print out the result

# question 21
def fun() :
    num = 5 #here set num to be 5
    def g() :
        num = 10 #here set num to be 10
        print(num, end =" ")#here print num, i.e. print(num, end= ' ')
    g()
    print(num) #here print name, i.e. print(num)
fun()

# question 22
x, y = 50, 60
def fun():
    global x
    y = 30
    x = x * 2
    y= y + 20
fun()
print(x, y)

# question 23
x = 10
y = 5
print("The result is: ", x + y if x >= y else x * y)

# question 24
'''
Write code to generate the following random values. You need to import the random module properly. No need to run your code.  
(1) gameScore = a random integer in the range [1000, 5000]
(2) myChoice is a random letter choice from a string "RPS", i.e. myChoice will be one of the letter 'P', 'R', or 'S'.
'''
import random
gameScore = random.randint(1000, 5000)
myChoice = random.choice("RPS")

# question 25
'''
for (int i = 0; i <= 50; i+=2) {
      for(int j = 1; j < i; ++j) {
           System.out.print(j + " ");
      }
      System.out.println();
  }
'''
for i in range(0, 51, 2):
    for j in range(1, i):
        print(f"{j}", end = " ")
    print("\n")