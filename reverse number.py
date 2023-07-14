class reverse:

    def __init__(self):
        self.user_number = int(input("Enter the number = "))
        self.number = 0
        

    def my_funct(self):
 
        while self.user_number != 0:
            self.number = self.number*10 + self.user_number%10
            self.user_number = self.user_number//10
        
        print(f"reversed number is {self.number}")


number1 = reverse()
number1.my_funct()



