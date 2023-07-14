import datetime


class health:
 
 def __init__(self):
    self.user = int(input("Enter your option = "))
    print("What do you wanna log, select your option from below")
    print("F for Food")
    print("E for Excersice")
    self.choice = input("Enter your option = ")
    self.date = datetime.datetime.now()
 
 def write(self):  
 
  if self.user == 1:
    if self.choice == "F" or self.choice == "f":
        rohan_food = open("rohan_food.txt", "a")
        rohan_food.writelines(f"\n{self.date}, ")
        rohan_food.writelines(input("Enter the data = "))
        rohan_food.close()
      
    elif self.choice == "E" or self.choice == "e":
        rohan_log = open("rohan_log.txt", "a")
        rohan_log.writelines(f"\n{self.date}, ")
        rohan_log.writelines(input("Enter the data = "))
        rohan_log.close()
      
    else:
        print("Invalid input")

  elif self.user == 2:
    if self.choice == "F" or self.choice == "f":
        raj_food = open("raj_food.txt", "a")
        raj_food.writelines(f"\n{self.date}, ")
        raj_food.writelines(input("Enter the data = "))
        raj_food.close()
      
    elif self.choice == "E" or self.choice == "e":
        raj_log = open("raj_log.txt", "a")
        raj_log.writelines(f"\n{self.date}, ")
        raj_log.writelines(input("Enter the data = "))
        raj_log.close()
      
    else:
        print("Invalid input")
        
  elif self.user == 3:
    if self.choice == "F" or self.choice == "f":
        lata_food = open("late_food.txt", "a")
        lata_food.writelines(f"\n{self.date}, ")
        lata_food.writelines(input("Enter the data = "))
        lata_food.close()
      
    elif self.choice == "E" or self.choice == "e":
        lata_log = open("lata_log.txt", "a")
        lata_log.writelines(f"\n{self.date}, ")
        lata_log.writelines(input("Enter the data = "))
        lata_log.close()
      
    else:
        print("Invalid input")
  else:
     print("Enter valid option")
     

 def read(self):
 
  if self.user == 1:
    if self.choice == "F" or self.choice == "f":
        rohan_food = open("rohan_food.txt", "r")
        rrf = rohan_food.readlines()
        print
        rohan_food.close()
      
    elif self.choice == "E" or self.choice == "e":
        rohan_log = open("rohan_log.txt", "r")
        rrl = rohan_log.readlines()
        print(rrl)
        rohan_log.close()
      
    else:
        print("Invalid input")

  elif self.user == 2:
    if self.choice == "F" or self.choice == "f":
        raj_food = open("raj_food.txt", "r")
        rf = raj_food.readlines()
        print(rf)
        raj_food.close()
      
    elif self.choice == "E" or self.choice == "e":
        raj_log = open("raj_log.txt", "r")
        rl = raj_log.readlines()
        print(rl)
        raj_log.close()
      
    else:
        print("Invalid input")
        
  elif self.user == 3:
    if self.choice == "F" or self.choice == "f":
        lata_food = open("late_food.txt", "r")
        lf =lata_food.readlines()
        print(lf)
        lata_food.close()
      
    elif self.choice == "E" or self.choice == "e":
        lata_log = open("lata_log.txt", "r")
        ll =lata_log.readlines()
        print(ll)
        lata_log.close()
      
    else:
        print("Invalid input")
  else:
     print("Enter valid option")




print("Welcome to Health Managment system")

select = int(input("Do you want write(1) or read(2) = "))

if select == 1:
       
       print("select your option from below")
       print("1 for Rohan")
       print("2 for Raj")
       print("3 for Lata")
          
       user1 = health()
       user1.write()

elif select == 2:
       
       print("select your option from below")
       print("1 for Rohan")
       print("2 for Raj")
       print("3 for Lata")

       user2 = health()
       user2.read()






    

        