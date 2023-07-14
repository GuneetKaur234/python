print("Welcome to Quiz")
list_questions = [["Which of these Superheroes is green in colour?", 'a. Aquaman' ,'b. Wonder Woman' ,'c. Incredible Hulk ','d. Black Window',"c"], ["Who is the superhero that is also known as the 'Man of Steel?'", 'a. Iron Man' ,'b. Captain America' ,'c. Superman ','d. Flash',"c"], ["Who was the first female superhero to appear in the title of an MCU film?", 'a. Black Widow' ,'b. Gamora' ,'c. Wasp ','d. Wanda Maximoff',"a"], ["Who was the first major character to die?",'a. Iron Man' ,'b. Gamora' ,'c. Black Window ','d. Heimdall',"a"]]

levels = [1000,2000,3000,4000]
list_answers = []

for x in range(0,len(list_questions)):
    print(f"Question for Rs {levels[x]} : \n {list_questions[x][0]}")
    print(f"{list_questions[x][1]}             {list_questions[x][2]}")
    print(f"{list_questions[x][3]}             {list_questions[x][4]}")
    answer = input(f"Enter the answer for Rs{levels[x]} = ")
    list_answers.append(answer)

    if list_answers[x] == list_questions[x][5]:
        print("Correct answer")
    else:
        print("Wrong answer")
        break


    
price = 0

for x in range(0,len(list_answers)):
    if list_answers[x] == list_questions[x][5]:
        price = price + int(levels[x])

print(f"Total price is {price}")



