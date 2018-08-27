# Multiple Choice Quiz
from Question import Question

question_prompts = [
    "What color are apples? \n(a) Red/Green \n(b) Purple \n(c) Orange \n\n",
    "What color are Bananas? \n(a) Teal \n(b) Brown \n(c) Yellow \n\n",
    "What color are Mangoes? \n(a) Black \n(b) Green \n(c) Orange \n\n"
    
    ]

questions = [
        Question(question_prompts[0], "a"),
 #       Question(question_prompts[-3], "A"),
        Question(question_prompts[1], "c"),
 #       Question(question_prompts[-1], "C"),
        Question(question_prompts[2], "b"),
 #       Question(question_prompts[-2], "B")
    ]

def run_test(questions): #create function, list of question objects we want to as the user
    score = 0
##    invalid_entries = 0
    
    for question in questions: #for each question object we want to run a question in the array
        answer = input(question.prompt) #answer student gives
        if answer == question.answer:
            score += 1
 #       elif answer == ["01234567899876543210"]:
 #           print("Invalid reposonse, Please try again!")
 #   for question in questions:
#        answer = input(question.prompt)
 #       if answer == invalid_entries:
 #           invalid_entries+= 3
 #           if invalid_entries <= 3:
 #       else:
 #           print("To many Invalid Entries, Please try again, using letters Lower Case!")
 #               for question in questions:
#                    invalid_answer = input(question.prompt)
        #break;
    print("Great; You got " + str(score) + "/" + str(len(questions)) + "Correct")
    
run_test(questions)