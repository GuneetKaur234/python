import math

alphbet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encryption(text,key):
    message = ""
    for x in text:
        if x in alphbet_list:
           position =alphbet_list.index(x)
           new_position = (position + shift_number)%26
           message += alphbet_list[new_position]

        else:
            message +=x


    
    print(f"Text after encryption {message}")


def decryption(text1,key1):
    message1 = ""
    for x in text1:
        if x in alphbet_list:
            position1 =alphbet_list.index(x)
            new_position1 = (position1 - shift_number)%26
            message1 += alphbet_list[new_position1]

        else:
            message1 += x
    
    print(f"Text after decryption {message1}")




statement = True
while statement:
    user_choice = input("Type 'E' for encryption and 'D' for decryption :")

    user_message = input("Enter your message :").lower()
    shift_number = int(input("Enter the shift number :"))

    if user_choice == "E" or user_choice == "e":
        encryption(user_message,shift_number)
    
    elif user_choice == "D" or user_choice =="d":
        decryption(user_message,shift_number)

    play_again = input("Do you want to continue Y/N:")

    if play_again == "n" or play_again == "N":
        statement = False
        print("thank you!")

    
        
