import random

print("Welcome to the Hangman game.")
print("Word will be selected by computer, you have only 6 lives to win this game.")

Words = ["apple", "beautiful","potato","hello","bicycle"]

lives = 6

rand_word = random.choice(Words)
print(rand_word)

blank = ""

for x in rand_word:
    x = "_"
    blank += x
   
print(f"Selected word is = {blank}")

blank_list = list(blank)
word_list = list(rand_word)

game_over = False

while not game_over:

    user_guess = input("Enter your guess = ").lower()

    for x in range(len(word_list)):
         letter = word_list[x]
         if letter == user_guess:
            blank_list[x] = user_guess
                   
    print(blank_list)
    
    if user_guess not in word_list:
        lives -= 1
        print(f"{lives} lives left ☠️") 

        if lives == 0:
            game_over = True

            print(f"Correct word was {rand_word}")
            print("You lose!")
       
    if "_" not in blank_list:
        game_over = True

        correct_word = ""
        
        for x in word_list:
            correct_word += x
        
        print(f"Correct word is {correct_word}")

        print("You Win!!")
    



    
   







    

