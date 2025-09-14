questions = (("What is the average world height: "),
             ("How many days does a non-leap year consist: "),
             ("Which is the strongest naturally occuring substance: "),
             ("Which color has the longest wavelenght: "),
             ("How many elemnets does the peroidic table conatin: "))
options = (("A. 160","B. 162","C. 163","D. 164"),
           ("A. 383","B. 365","C. 400","D.290"),
           ("A. Diamond","B. Iron","C. Obsadian","D. Wood"),
           ("A. Black","B. Orange","C. Purple","D. Red"),
           ("A. 155","B. 118","C. 160","D. 96"))
ques_num = 0
score=0
guesses=[]
answers=('C','B','A','D','B')
for question in questions:
  print("--------------------------------")
  print(question)

  for option in options[ques_num]:
    print(option)

  guess=input("Enter (A, B, C, D): ").upper()
  guesses.append(guess)
  if guess == answers[ques_num]:
    score+=1
    print('Correct')
  else:
    print('Incorrect')
    print(f"{answers[ques_num]} is the Correct answer")

  ques_num+=1

print('------------------------')
print('--------Results---------')
print('------------------------')
print('Answers: ',end="")
for answer in answers:
  print(answer,end=" ")
print() 

print('Guesses: ',end="")
for guess in guesses:
  print(guess,end=" ")
print()  
print(f'Your score is: {(score/len(questions)*100)}')