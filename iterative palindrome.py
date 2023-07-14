number = int(input("Enter the number to check if it is a Palindrome = "))
temp = number
reverse = 0

while temp!= 0:
    
        reverse = reverse *10 + temp%10
        temp = temp//10

if reverse == number:
            print("Number is palindrom")

else:
            print("Number is not palindrome")