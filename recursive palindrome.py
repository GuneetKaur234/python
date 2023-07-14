def reverse(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(reverse(n//10)))


def ispalin(n):
    if n == reverse(n):
        return 1
    
    return 0


number = int(input("Enter the number to check if it is a Palindrome = "))

if ispalin(number) == 1:
    print("Nummber is Plaindrome")
else:
    print("Number is not Palindrome")