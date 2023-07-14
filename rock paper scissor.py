import random

Rock = str("🪨")
Paper = str("📃")
Scissor = str("✂️")

Game_choice = [Rock,Paper,Scissor]

print("Please select your choice :")
User_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissor = "))

computer_choice = random.randint(0,2)

print(f"User has choosen : {Game_choice[User_choice]}")
print(f"Computer chose : {Game_choice[computer_choice]}")


if User_choice >= 3 or User_choice < 0:
        print("Error☠️, please select correct option") 
    
else:
    
        if User_choice == 2 and computer_choice == 0:
           print("You lose😭")
        
        elif User_choice == 0 and computer_choice == 2:
           print("You wins🥳")

        elif User_choice == computer_choice:
            print("Draw match, no one wins💀")

        elif User_choice > computer_choice:
            print("You wins🥳")

        elif User_choice < computer_choice:
            print("You lose😭")











    

    





