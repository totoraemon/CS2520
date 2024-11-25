# Question 16
line = "today  ,   is,     a ,  beautiful     , day"
words = line.replace(" ", "").split(",")
wordSize = [len(word) for word in words]
print(words)        # not submitted for exam
print(wordSize)     # not submitted for exam

# Question 17
t = set()
words = ["bye", "sad", "happy"]
for w in words:
    t.add(w)
s = {"bye", "hi", "good", "okay", "sad"} 
w = s & t
print(", ".join(f"{val}" for val in w))

# Question 18
fruitList = ["melon", "banana", "banana", "melon", "apple", "melon", "cherry"]
uniqFruit = set(fruitList)
fruits = {}

for uniq in uniqFruit:
    fruits[uniq] = 0

for fruit in fruitList:
    fruits[fruit] += 1

sortFruit = sorted(fruits)
print(sortFruit)

print("Number of fruits: ", len(fruitList))

# Question 19
try:
    inf = open("data.txt", "r")
    for line in inf:
        try:
            value = float(line.strip())
        except ValueError:
            print("Wrong data format")
        except Exception:
            print("unexpected error")
        else:
            print("Good")

finally:
    inf.close()
    print("Done")

# Question 20
import random
nameLst = ['Kevin', 'Ada', 'Jenny', 'Ade', 'Betty', 'Sam', 'Kenny', 'Beta', 'Berry', 'Terry', 'Nathan', 'Jess']
ageLst = [random.randint(18, 25) for val in range(len(nameLst))]
infoLst = list(zip(nameLst, ageLst))
print(infoLst)

sortName = sorted(infoLst)
print(sortName)

sortAge = sorted(infoLst, key = lambda x: x[1], reverse = True)
print(sortAge)