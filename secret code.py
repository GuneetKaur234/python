import string
import random

def encryption(text):
    message = ""
    random_message = ""
    n = 2
    for x in text:
        message = text[::-1]
        random_message = message.join(random.choices(string.ascii_lowercase,k=n))
        random_message = random_message.join(random.choices(string.ascii_lowercase,k=n))
        random_message = random_message.join(random.choices(string.ascii_lowercase,k=n))

    print(f"Encryted message is {random_message}")


def decryption(text):
    message = text[3:-3]
    message = message[::-1]      
    print(message)


statement = True
while statement:
    user_choice = input("Type 'E' for encryption and 'D' for decryption :")

    user_message = input("Enter your message :").lower()

    if user_choice == "E" or user_choice == "e":
        encryption(user_message)
    
    elif user_choice == "D" or user_choice =="d":
        decryption(user_message)

    play_again = input("Do you want to continue Y/N:")

    if play_again == "n" or play_again == "N":
        statement = False
        print("thank you!")