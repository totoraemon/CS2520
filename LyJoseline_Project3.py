# Name : Joseline Ly
import string       # used for task1()
import statistics   # used for task2()

# Project 3 Task 1
def task1():
    "This program reads a file, logs all the words into a list, stores unique words in a set, and puts them as a key with their frequency as a value in a dictionary."
    # Task 1.1 and 1.2 - open a file titled "article.txt" in read mode
    # article.txt contains text from given link up until the number 71 is seen
    article = open("article.txt", "r")
    
    # Task 1.3 - remove punctuation from each line and save words into a list
    listWords = []
    for line in article:
        words = line.translate(str.maketrans('', '', string.punctuation + string.digits)).lower().split()
        listWords.extend(words)
    article.close()

    # Task 1.4 - create a set holding unique words from the list of words
    uniq = set(listWords)
    
    # Task 1.5 - create a dictionary with word as key and frequency as value
    dictWords = {}
    for w in listWords:
        if w in dictWords:
            dictWords[w] += 1
        else:
            dictWords[w] = 1
    
    # Task 1.6 - remove all conjunction words and 'a', 'an', 'to', 'in', and 'at' from word list, sorts and prints out first 100 words with 20 per line
    rm = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so', 'a', 'an', 'to', 'in', 'at']
    sortWords = sorted([word for word in uniq if word not in rm])

    print("First 100 Unique Words (Alphabetical Order):")
    for i in range(0, min(100, len(sortWords)), 20):
        print(", ".join(sortWords[i : i + 20]))
    print()

    # Task 1.7 - remove all words in list rm from dictWords, print 50 most frequent words in form of tuples in descending order with 10 per line
    sortDict = {word: freq for word, freq in dictWords.items() if word not in rm}
    sortedDict = sorted(sortDict.items(), key = lambda item : item[1], reverse = True)

    print("50 Most Frequent Words (Descending Order):")
    for i in range(0, min(50, len(sortedDict)), 10):
        tupleDict = [(word, freq) for word, freq in sortedDict[i : i + 10]]
        print(", ".join(f"{tup}" for tup in tupleDict))
    print()

# Project 3 Task 2
def task2():
    '''
    This program takes a list of names and scores and returns a list of tuples and a dictionary with names for keys and scores for values.
    It defines methods setup(), score_update(), and get_stat().
    '''
    # Task 2.1 - create function setup() that takes 2 lists as parameters and returns 2 values (list of tuples and adictionary)
    def setup(names, scores):
        tupList = list(zip(names, scores))
        dictNS = {}
        for i in range(len(names)):
            dictNS[names[i]] = scores[i]
        return tupList, dictNS

    # Task 2.2 - create function score_update() that takes a dictionary, a student's name, and a score to update
    def score_update(dictUpdate, studentName, newScore):
        if (studentName in dictUpdate):
            dictUpdate[studentName] = newScore
            return("Done")
        else:
            print("Student's score could not be updated. Please check inputted values.")
            return None
    
    # Task 2.3 - create function get_stat() that returns average, standard deviation, and highest score
    def get_stat(classDict):
        classAvg = round(sum(classDict.values()) / len(classDict), 2)
        classDev = round(statistics.stdev(classDict.values()), 2)
        orderedDict = sorted(classDict.items(), key = lambda item : item[1], reverse = True)
        classHigh = orderedDict[0] if orderedDict else (None, None)
        return classAvg, classDev, classHigh

    # Test Run with Provided Lists
    listNames1 = ["Andy", "Ben", "Cathy", "Dave", "Edward", "Fanny", "George", "Hana", "Jess", "Karen", "Nancy", "Pedro"]
    listScores1 = [88, 92, 85, 76, 85, 96, 77, 82, 90, 72, 98, 82]
    tupScores, dictScores = setup(listNames1, listScores1)
    print(f"Scores as Tuples: {tupScores}")         # Result of setup()
    print(f"Scores as Dictionary: {dictScores}")    # Result of setup()

    score_update(dictScores, "Andy", 95)            # Testing existing name
    print(f"Update Andy to 95: {dictScores}")       # Result of score_update()
    score_update(dictScores, "Andrew", 95)          # Testing non-existent name
    print(f"Update Andrew to 95: {dictScores}")     # Result of score_update()

    avgScore, stdDev, highScore = get_stat(dictScores)
    print(f"Class Average: {avgScore}, Class Std. Deviation: {stdDev}, Class High: {highScore}")    # Result of get_stat()
    print()     # For formatting purposes

    # Test Run with Self-Made Lists
    listNames2 = ["Andy", "Ben", "Cathy", "Dave", "Edward", "Fanny", "George", "Hana", "Ian", "Jess", "Karen", "Lucy", "Nancy", "Pedro", "Ryan", "Romero", "Sally", "Steven", "Suzy", "Tim"]
    listScores2 = [94, 95, 90, 82, 83, 76, 87, 83, 93, 99, 86, 79, 82, 89, 98, 91, 92, 78, 84, 81]
    tupScores, dictScores = setup(listNames2, listScores2)
    print(f"Scores as Tuples: {tupScores}")         # Result of setup()    
    print(f"Scores as Dictionary: {dictScores}")    # Result of setup()

    score_update(dictScores, "Cathy", 95)           # Testing existing name
    print(f"Update Andy to 95: {dictScores}")       # Result of score_update()
    score_update(dictScores, "Edward", 88)          # Testing existing name
    print(f"Update Andrew to 95: {dictScores}")     # Result of score_update()

    avgScore, stdDev, highScore = get_stat(dictScores)
    print(f"Class Average: {avgScore}, Class Std. Deviation: {stdDev}, Class High: {highScore}")    # Result of get_stat()
    print()     # For formatting purposes

# Project 3 Task 3
def main():
    "main() calls task1() and task2()"
    task1()
    #task2()

main()

'''
Test Run for task1()
First 100 Unique Words (Alphabetical Order):
abide, about, above, absence, absent, abundance, abuse, accents, acceptable, accepts, access, accessary, account, accusing, achieve, acknowledge, acquainted, action, active, actor
add, adding, addition, additional, adieu, admiring, adonis, adore, adoting, advantage, adverse, advised, advisor, advocate, affairs, afresh, after, again, against, age
agents, ages, agree, ah, air, alack, alchemy, alive, all, allayed, alleating, allege, alloblivious, allow, allowable, allowed, almost, alone, also, alter
alteration, alternatively, although, am, amazeth, ambush, amis, amiss, among, analyzed, anger, annoy, anon, anonymous, another, anothers, answer, answers, antique, antiquity      
any, anyone, apparel, appear, appearance, appetite, apply, approve, april, aprils, archives, are, argument, arise, arising, art, as, ascii, asis, asked

50 Most Frequent Words (Descending Order): 
('the', 276), ('of', 227), ('my', 154), ('that', 145), ('i', 129), ('thy', 127), ('thou', 120), ('with', 108), ('is', 90), ('you', 80)
('by', 78), ('thee', 76), ('be', 75), ('this', 74), ('not', 72), ('love', 67), ('when', 63), ('all', 62), ('his', 59), ('your', 58)
('as', 57), ('me', 54), ('it', 53), ('from', 50), ('self', 47), ('do', 46), ('which', 46), ('are', 43), ('on', 43), ('then', 41)
('doth', 41), ('time', 39), ('if', 37), ('no', 35), ('shall', 34), ('mine', 34), ('beauty', 33), ('one', 31), ('art', 31), ('may', 30)
('should', 29), ('more', 29), ('their', 28), ('have', 28), ('can', 28), ('eyes', 28), ('thine', 27), ('etext', 25), ('what', 25), ('sweet', 25)


Test Run for task2()
Scores as Tuples: [('Andy', 88), ('Ben', 92), ('Cathy', 85), ('Dave', 76), ('Edward', 85), ('Fanny', 96), ('George', 77), ('Hana', 82), ('Jess', 90), ('Karen', 72), ('Nancy', 98), ('Pedro', 82)]   
Scores as Dictionary: {'Andy': 88, 'Ben': 92, 'Cathy': 85, 'Dave': 76, 'Edward': 85, 'Fanny': 96, 'George': 77, 'Hana': 82, 'Jess': 90, 'Karen': 72, 'Nancy': 98, 'Pedro': 82}
Update Andy to 95: {'Andy': 95, 'Ben': 92, 'Cathy': 85, 'Dave': 76, 'Edward': 85, 'Fanny': 96, 'George': 77, 'Hana': 82, 'Jess': 90, 'Karen': 72, 'Nancy': 98, 'Pedro': 82}
Student's score could not be updated. Please check inputted values.
Update Andrew to 95: {'Andy': 95, 'Ben': 92, 'Cathy': 85, 'Dave': 76, 'Edward': 85, 'Fanny': 96, 'George': 77, 'Hana': 82, 'Jess': 90, 'Karen': 72, 'Nancy': 98, 'Pedro': 82}
Class Average: 85.83, Class Std. Deviation: 8.46, Class High: ('Nancy', 98)

Scores as Tuples: [('Andy', 94), ('Ben', 95), ('Cathy', 90), ('Dave', 82), ('Edward', 83), ('Fanny', 76), ('George', 87), ('Hana', 83), ('Ian', 93), ('Jess', 99), ('Karen', 86), ('Lucy', 79), ('Nancy', 82), ('Pedro', 89), ('Ryan', 98), ('Romero', 91), ('Sally', 92), ('Steven', 78), ('Suzy', 84), ('Tim', 81)]
Scores as Dictionary: {'Andy': 94, 'Ben': 95, 'Cathy': 90, 'Dave': 82, 'Edward': 83, 'Fanny': 76, 'George': 87, 'Hana': 83, 'Ian': 93, 'Jess': 99, 'Karen': 86, 'Lucy': 79, 'Nancy': 82, 'Pedro': 89, 'Ryan': 98, 'Romero': 91, 'Sally': 92, 'Steven': 78, 'Suzy': 84, 'Tim': 81}
Update Andy to 95: {'Andy': 94, 'Ben': 95, 'Cathy': 95, 'Dave': 82, 'Edward': 83, 'Fanny': 76, 'George': 87, 'Hana': 83, 'Ian': 93, 'Jess': 99, 'Karen': 86, 'Lucy': 79, 'Nancy': 82, 'Pedro': 89, 'Ryan': 98, 'Romero': 91, 'Sally': 92, 'Steven': 78, 'Suzy': 84, 'Tim': 81}
Update Andrew to 95: {'Andy': 94, 'Ben': 95, 'Cathy': 95, 'Dave': 82, 'Edward': 88, 'Fanny': 76, 'George': 87, 'Hana': 83, 'Ian': 93, 'Jess': 99, 'Karen': 86, 'Lucy': 79, 'Nancy': 82, 'Pedro': 89, 'Ryan': 98, 'Romero': 91, 'Sally': 92, 'Steven': 78, 'Suzy': 84, 'Tim': 81}
Class Average: 87.6, Class Std. Deviation: 6.86, Class High: ('Jess', 99)
'''
