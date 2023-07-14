F_name = input("Enter the female name = ")
M_name = input("Enter the male name = ")

f_name = F_name.lower()
m_name = M_name.lower()


T = f_name.count("t") + m_name.count("t")
R = f_name.count("r") + m_name.count("r") 
U = f_name.count("u") + m_name.count("u") 
E = f_name.count("e") + m_name.count("e") 

L = f_name.count("l") + m_name.count("l")
O = f_name.count("o") + m_name.count("o") 
V = f_name.count("v") + m_name.count("v")
e = f_name.count("e") + m_name.count("e") 

add_true = T + R + U + E
add_love = L + O + V + e

love_cal = add_true*10 + add_love

if love_cal < 10:
    print(f"You are not compatible, your love score is {love_cal}%")

elif love_cal < 40:
    print(f"Your love score is {love_cal}%")

elif love_cal < 60:
    print(f"Need some work,your love score is {love_cal}%")

elif love_cal < 90:
    print(f"can work out,your love score is {love_cal}%")

else:
    print(f"You are compatible, your love score is {love_cal}% ")

print("Thank you! please visit again")
