user_email = input("Enter your Email ID: ")
user_email = user_email.split("@")
user_name = user_email[0]
domain_name = user_email[1]

print(f"User name is {user_name}")
print(f"Domian name is {domain_name}")