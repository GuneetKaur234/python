number = int(input("Enter  the number = "))
boolean = int(input("numbers should be 0 or 1 = "))

char = "*"
for x in range(1,number+1):
    if boolean == 1:
        if x == 0:
            pass
        else:
            print(f"{char*x}")
    elif boolean == 0:
        if x == 0:
            pass
        else:
           print(f"{char*(number+1-x)}")
