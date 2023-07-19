import random

print("Lets start the game!!")

animal_list = ["dog","cat","lion","cow"]

comp_animal = random.choice(animal_list)
print(comp_animal)

for x in range(0,4):
    if x == 0:
      if comp_animal == animal_list[x]:
        print(f"hint 1")
        print("mans best frnd")
        dog1 = input("enter your answer :")
        

        if dog1 == "dog":
            print("you win")

        else:
            print(f"chances left {3-1}")
            print(f"hint 2")
            print("found in almost every home")
            dog2 = input("enter your answer :")
            

            if dog2 == "dog":
               print("you win")
            
            else:
              print(f"chances left {3-2}")
              print(f"hint 3")
              print("does bow bow")
              dog3 = input("enter your answer :")

              if dog3 == "dog":
               print("you win")

              else:
                 print("you lose")

    elif x == 1:
      if comp_animal == animal_list[x]:
        print(f"hint 1")
        print("is selfish")
        cat1 = input("enter your answer :")
        

        if cat1 == "cat":
            print("you win")

        else:
            print(f"chances left {3-1}")
            print(f"hint 2")
            print("found in some homes")
            cat2 = input("enter your answer :")
            

            if cat2 == "cat":
               print("you win")
            
            else:
              print(f"chances left {3-2}")
              print(f"hint 3")
              print("does mewo mewo")
              cat3 = input("enter your answer :")

              if cat3 == "cat":
               print("you win")

              else:
                 print("you lose")
    
    elif x == 2:
      if comp_animal == animal_list[x]:
        print(f"hint 1")
        print("is strong")
        lion1 = input("enter your answer :")
        

        if lion1 == "lion":
            print("you win")

        else:
            print(f"chances left {3-1}")
            print(f"hint 2")
            print("found in some homes")
            lion2 = input("enter your answer :")
            

            if lion2 == "lion":
               print("you win")
            
            else:
              print(f"chances left {3-2}")
              print(f"hint 3")
              print("does mewo mewo")
              lion3 = input("enter your answer :")

              if lion3 == "lion":
               print("you win")

              else:
                 print("you lose")

    elif x == 3:
      if comp_animal == animal_list[x]:
        print(f"hint 1")
        print("is strong")
        cow1 = input("enter your answer :")
        

        if cow1 == "cow":
            print("you win")

        else:
            print(f"chances left {3-1}")
            print(f"hint 2")
            print("found in some homes")
            cow2 = input("enter your answer :")
            

            if cow2 == "cow":
               print("you win")
            
            else:
              print(f"chances left {3-2}")
              print(f"hint 3")
              print("does mewo mewo")
              cow3 = input("enter your answer :")

              if cow3 == "cow":
               print("you win")

              else:
                 print("you lose")

            


    