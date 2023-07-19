user_email = input("Enter the your Email address : ").lower()
domain_name = ["gmail.com","yahoo.com","outlook.com","microsoft.com"]

if "@" in user_email:
    split_email = user_email.split("@")
    if split_email[1] in domain_name:
        if "."in split_email[0]:
            user_name = split_email[0].split(".")
            if user_name[0].isalnum() and user_name[1].isalpha():
                print("Valid Email address")

            else:
                print("Invalid Email ID")
                
        elif "_" in split_email[0]:
            user_name = split_email[0].split("_")
            if user_name[0].isalnum() and user_name[1].isalpha():
                print("Valid Email address")

            else:
                print("Invalid Email ID")


        else:
            print("Invalid Email ID")
    
    else:
        print("Invalid Email ID")


else:
    print("Invalid Email ID")

