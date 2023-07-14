class cal:

    def __init__(self):
        self.a = int(input("Enter the first number = "))
        self.b = int(input("Enter the second number = "))
        self.op = (input("Enter the operator = "))\
        
    def calculator(self):
        
    
          if self.a == 45 and self.b == 3 and self.op =="*":
            print("result is 555")

          elif self.a == 56 and self.b == 9 and self.op =="+":
            print("result is 77")

          elif self.a == 56 and self.b == 6 and self.op =="/":
            print("result is 4")

          elif self.op == "+":
            print(f"result is {self.a + self.b} ")

          elif self.op == "-":
            print(f"result is {self.a - self.b} ")

          elif self.op == "*":
            print(f"result is {self.a * self.b} ")

          elif self.op == "/":
            print(f"result is {self.a / self.b} ")

          else:
            print("invalid input")
        



print("Operation you can perform are : ")
print("+ for Addition")
print("- for Addition")
print("* for Addition")
print("/ for Addition")

user = cal()
user.calculator()


while True:
   user_wish = input("Do you want to continue Y/N :")
   if user_wish == "Y" or user_wish == "y" :
    user2 = cal()
    user2.calculator()
   else:
     print("thank you")
     break