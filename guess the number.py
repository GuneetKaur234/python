
number = 18
sum = 0

for x in range(1,10):
    
    print(f"try {x}")
    sum = sum = x
    user_guess = int(input("Enter the number = "))
    if user_guess < number:
       print("guessed number is less than correct number.")
       print(f"number of guesses left are {9-int(x)}")

    elif user_guess > number:
       print("guessed number is greater than correct number.")
       print(f"number of guesses left are {9-int(x)}")

    elif user_guess == number:
       print("correct guess")
       print("you win")
       print(f"user gussed the correct number in {x} guesses")
       break

else:
   print("you lose")  
