# Name : Joseline Ly
# Lab 5 Task 1

import random   # used for create_test

class Question:
    def __init__(self, question_num, question_text, ans_choice1, ans_choice2, ans_choice3, ans_choice4, correct_ans):
        """ Each instance of the class Question will have the question, 4 answer choices, and the correct answer. """
        self.question_num = question_num
        self.question_text = question_text
        self.ans_choice1 = ans_choice1
        self.ans_choice2 = ans_choice2
        self.ans_choice3 = ans_choice3
        self.ans_choice4 = ans_choice4
        self.correct_ans = correct_ans

    def __str__(self):
        """ This definition will override the print() function and display the answers in a readable format."""
        return (f"\tA. {self.ans_choice1}\n"
                f"\tB. {self.ans_choice2}\n"
                f"\tC. {self.ans_choice3}\n"
                f"\tD. {self.ans_choice4}\n")
    
def create_questions():
    """ This function creates a question bank of 10 questions to be selected for the test. """
    # Create a list to hold all the questions
    question_bank = []
    
    # Create and add question objects to the question bank
    question_bank.append(Question(1, "Where is Cal Poly Pomona located?", "Texas", "California", "Nevada", "Washington", "California"))
    question_bank.append(Question(2, "What is the mascot of Cal Poly Pomona?", "Mustang", "Lion", "Eagle", "Wolf", "Mustang"))
    question_bank.append(Question(3, "Which college at Cal Poly Pomona focuses on engineering?", "College of Business Administration", "College of Engineering", "College of Letters, Arts, and Social Sciences", "College of Environmental Design", "College of Engineering"))
    question_bank.append(Question(4, "What is the name of the main library at Cal Poly Pomona?", "University Library", "The Bronco Library", "The Pomona Library", "The California Library", "University Library"))
    question_bank.append(Question(5, "Which year was Cal Poly Pomona founded?", "1901", "1949", "1938", "1960", "1938"))
    question_bank.append(Question(6, "Who was the first president of Cal Poly Pomona?", "Charles B. Ream", "Harry S. Truman", "Albert Einstein", "Donovan G. Davis", "Charles B. Ream"))
    question_bank.append(Question(7, "What is the official school color of Cal Poly Pomona?", "Blue and Gold", "Red and Black", "Green and Gold", "Bronco Blue and Green", "Green and Gold"))
    question_bank.append(Question(8, "What is the name of the farm located at Cal Poly Pomona?", "The CPP Farm", "The Pomona Valley Farm", "The Lyle Center for Regenerative Studies", "The Agriscapes", "The Agriscapes"))
    question_bank.append(Question(9, "What is the name of the Cal Poly Pomona student-run farm?", "Bronco Farm", "The Pomona Farm", "CPP Organic Farm", "Cal Poly Pomona Farm", "CPP Organic Farm"))
    question_bank.append(Question(10, "What is the name of the student newspaper at Cal Poly Pomona?", "The Poly Post", "Bronco Times", "The Mustang News", "The CPP Chronicle", "The Poly Post"))
    return question_bank

def create_test(question_bank):
    """ This function creates a test of 5 questions that are randomly selected from the question bank."""
    test_questions = random.sample(question_bank, 5)    # selects 5 random questions from question_bank
    return test_questions

class Student():
    def __init__(self, name, id_num):
        """ Initializes a Student's name and ID to the provided values, and test score that is set to 0."""
        self.name = name
        self.id_num = id_num
        self.score = 0
    
    def take_test(self, test_questions):
        """ Creates format for Student to take test and evaluates their score accordingly. """
        for index, question in enumerate(test_questions):   
            print(f"Q{index + 1}: {question.question_text} (Q{question.question_num} was selected)")  # displays the question order in the test and mentions which question was selected from the bank
            print(question)
            answer = input("Your answer: ").strip()  # get the student's answer as a full text (e.g. 'Texas')
            if answer.lower() == question.correct_ans.lower():  
                self.score += 1
            print()

    def show_score(self):
        """ Displays the Student's score out of 5. """
        print(f"\n{self.name}'s Score: {self.score}/5\n")

def main():
    """ Creates question bank, selects 5 random ones to test the student, creates the Student, calls take_test(), and displays Student's score."""
    question_bank = create_questions()
    test_questions = create_test(question_bank)
    student = Student("Joseline Ly", "017241510")
    student.take_test(test_questions)
    student.show_score()

main()

'''Test Run:
Q1: What is the name of the Cal Poly Pomona student-run farm? (Q9 was selected)
        A. Bronco Farm
        B. The Pomona Farm     
        C. CPP Organic Farm    
        D. Cal Poly Pomona Farm

Your answer: CPP Organic Farm

Q2: What is the name of the farm located at Cal Poly Pomona? (Q8 was selected)
        A. The CPP Farm
        B. The Pomona Valley Farm
        C. The Lyle Center for Regenerative Studies
        D. The Agriscapes

Your answer: CPP Farm

Q3: Who was the first president of Cal Poly Pomona? (Q6 was selected)
        A. Charles B. Ream
        B. Harry S. Truman
        C. Albert Einstein
        D. Donovan G. Davis

Your answer: Charles B. Ream

Q4: What is the name of the main library at Cal Poly Pomona? (Q4 was selected)
        A. University Library
        B. The Bronco Library
        C. The Pomona Library
        D. The California Library

Your answer: University Library

Q5: What is the official school color of Cal Poly Pomona? (Q7 was selected)
        A. Blue and Gold
        B. Red and Black
        C. Green and Gold
        D. Bronco Blue and Green

Your answer: Green and Gold


Joseline Ly's Score: 4/5
'''