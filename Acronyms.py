def acronyms():

   user = input("Enter the sentnce : ")
   user = user.split( " " )


   user_list = []

   for x in user:
    first = x[0]
    user_list.append(first)

   second = ""

   for x in user_list:
    second = second + x

   print(f"Computer generated acronyms is : {second.upper()}")


while True:
  user_input = input("Do you wnat to try getting an Acronyms (y/n) : ")

  if user_input == "Y" or user_input == "y":
    acronyms()
  else:
    print("Thank you! ")
    break