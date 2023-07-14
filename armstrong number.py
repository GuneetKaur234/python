class armstrong:
    
    def __init__(self):
        self.user_number = int(input("Enter the number to check if it is an armstrong number = "))
        self.temp= self.user_number
        self.n = 0
        self.count= len(str(self.user_number))

    def user_list(self):

        while self.temp != 0:
            digit = self.temp % 10
            self.n += digit ** self.count
            self.temp //= 10

        if self.user_number == self.n:
            print(f"given number {self.user_number} is an Armstrong number.")

        else:
            print(f"given number {self.user_number} is not an Armstrong number.")
    


user = armstrong()
user.user_list()


