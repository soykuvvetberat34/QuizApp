#Quiz examples


class Quiz(object):
    def __init__(self,questions,choices,true_choice):
        self.questions=questions
        self.choices=choices
        self.true_choice=true_choice
    
    def chechkAnswer(self,answer):
        self.answer=answer
        if (answer==self.true_choice):
            print("true")
        else:
            print("false")        

q1=Quiz("Which one is the best food?",["kebab","doner","taco","sushi"],"kebab")
q2=Quiz("Which country's capital Berlin?",["Turkey","Usa","Germany","Italy"],"Germany")
q3=Quiz("What is the 2*2?",[2,3,4,5],"4")
q4=Quiz("What is the 2*(5+6)-5",[15,16,17,18],"17")

q_list=[q1,q2,q3,q4]
q_list_questions=[q1.questions,q2.questions,q3.questions,q4.questions]
q_list_choices=[q1.choices,q2.choices,q3.choices,q4.choices]
q_list_true_choice=[q1.true_choice,q2.true_choice,q3.true_choice,q4.true_choice]



class MainQuiz(Quiz):
    def asking(self,user_choice):
        self.user_choice=user_choice
        
i=0
for q in q_list:
    try1=MainQuiz(q_list_questions,q_list_choices,q_list_true_choice[i])
    print("\n")
    print(f"--------Question {i+1}-------- ")
    print("-",q.questions)
    print(f"Choices: {q_list_choices[i]}")
    user_choice=input("what is your answer:")
    try1.chechkAnswer(user_choice)
    print("\n")
    print()
    i+=1



        
        
        
        
        
        
        
        
        
        
                 
