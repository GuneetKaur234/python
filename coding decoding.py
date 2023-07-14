import string
import random


def encryption(text):
    message = []
    for x in text:
        if len(x)>=3:
            n =3
            r1 = "nji"
            r2 = "dse"
            str = r1 + x[1:] + x[0] +r2
            message.append(str)
        
        else:
            message.append(x[::-1])
    
    print(" ".join(message))


def decryption(text):
    message = []
    for x in text:
        if len(x)>=3:
            str = x[3:-3]
            str = str[-1] + str[:-1]
            message.append(str)
        
        else:
            message.append(x[::-1])
    
    print(" ".join(message))







statement = True
while statement:
    user_choice = input("Type 'E' for encryption and 'D' for decryption :")

    user_message = input("Enter your message :").lower()
    list_message = user_message.split(" ")

    if user_choice == "E" or user_choice == "e":
        encryption(list_message)
    
    elif user_choice == "D" or user_choice =="d":
        decryption(list_message)

    play_again = input("Do you want to continue Y/N:")

    if play_again == "n" or play_again == "N":
        statement = False
        print("thank you!")