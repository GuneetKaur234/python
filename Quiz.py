print("Welcome to Quiz")
list_question = ["Which of these Superheroes is green in colour?", "Who is the superhero that is also known as the 'Man of Steel?'", "Who was the first female superhero to appear in the title of an MCU film?", "Who was the first major character to die?"]
list_options = [['1. Aquaman' ,'2. Wonder Woman' ,'3. Incredible Hulk ','4. Black Window'], ['1. Iron Man' ,'2. Captain America' ,'3. Superman ','4. Flash'], ['1. Black Widow' ,'2. Gamora' ,'3. Wasp ','4. Wanda Maximoff'], ['1. Iron Man' ,'2. Gamora' ,'3. Black Window ','4. Heimdall']]


user_question = int(input("Enter the question number from 1 to 4 = "))

print(f" Question{user_question}. {list_question[user_question - 1]}")
print(f" Options are {list_options[user_question - 1]}")

user_anwser = int(input("Enter your answer [1,2,3 or 4] = "))
print(f"Option selected by user is \n {list_options[user_question - 1][user_anwser - 1]}")

#for x in range(0,len(list_question)+1):
  
if user_question==1:
    if user_anwser == 3:
        print("Correct answer")

    else:
        print("Wrong answer")

elif user_question==2:
    if user_anwser == 3:
        print("Correct answer")

    else:
        print("Wrong answer")

elif user_question==3:
    if user_anwser == 1:
        print("Correct answer")

    else:
        print("Wrong answer")

elif user_question==4:
    if user_anwser == 1:
        print("Correct answer")

    else:
        print("Wrong answer")