def myfunct(n):
    if n == 0:
        return 1
    
    if n > 0:
        return n * myfunct(n-1)

try:
 number = int(input("Enter the number = ")) 
 print (f"Factorial of {number} is = {myfunct(number)}")  


except ValueError:
    print("Number entered is not an integer.")

print("end of program")  