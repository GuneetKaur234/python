import string

f = open("palindrome_data.txt","w")
w = f.writelines(input("Enter values = "))
f.close()

number = int(input("number of values entered = "))

f = open("palindrome_data.txt","rt")
line = f.readline()
word = []
for x in range(0,number):
     m = line.split(",")[x]
     word.append(m)
print(word)

result = list(filter(lambda x : x == x[::-1],word))
print(f"{result} is palindrome")
f.close()

