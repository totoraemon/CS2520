import random
nameLst = ['Kevin', 'Ada', 'Jenny', 'Ade', 'Betty', 'Sam', 'Kenny', 'Beta', 'Berry', 'Terry', 'Nathan', 'Jess']
ageLst = [random.randint(18, 25) for val in range(len(nameLst))]
infoLst = zip(nameLst, ageLst)
print("List of Zip Tuples:")
print(", ".join(f"{tup}" for tup in infoLst))

sortName = sorted(infoLst)
print("List of Sorted Tuples (Name):")
print(", ".join(f"{tup}" for tup in sortName))

sortAge = sorted(infoLst, reverse = True)