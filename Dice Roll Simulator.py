import random
from pygame import mixer

print("Welcome to Dice Roll Simulator")

    


while True:
    user = input("Do you wnat to roll the dice (y/n) : ")
    
    if user == "Y" or user == "y":
       print(f"The number is {random.randint(1,6)}")
       mixer.init()
       mixer.music.load("drinking water.mp3")
       mixer.music.play()
        
    
    else:
        print("Thank you")
        break

