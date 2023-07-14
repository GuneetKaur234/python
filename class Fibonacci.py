class fibonacci:

    def __init__(self):
        self.num = int(input("Enter the number for Fibonacci series = "))
        self.num0 = 0
        self.num1 = 1

    
    def my_funct(self):
        
        if self.num == 0:
            print("Fibonacci series is")
            print("0")
            return 0

        elif self.num == 1:
            print("Fibonacci series is")
            print("0")
            print("1")
            return 1
    
        else:

            print(self.num0)
            print(self.num1)

            for x in range(2,self.num):
                c = self.num0 + self.num1
                self.num0 = self.num1
                self.num1 = c

                print(c)



number = fibonacci()
number.my_funct()




    