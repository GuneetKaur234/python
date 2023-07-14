number = int(input("Enter the value of n = "))

list_number = range(1,number+1)


for x in list_number:

    if x%3 == 0 and x%5 ==0:
        print("FizzBuzz")

    elif x%3 == 0:
        print("Fizz")

    elif x%5 == 0:
        print("Buzz")

    else:
        print(x)

