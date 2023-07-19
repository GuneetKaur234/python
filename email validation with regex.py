import re


email_condition = "\w+[\._]?+[a-b  0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter the your Email address : ").lower()

if re.search(email_condition,user_email):        
        print("Valid Email address")

else:
        print("Invalid Email ID")
