
with open ("currency.txt") as curr:
    a = curr.readlines()

list = []
for x in a:
    split_curr = x.split("\t")
    list.append(split_curr)

dict = {}

for x in range(0,len(list)):
    list[x].pop(2)
    dict[list[x][0]] = float(list[x][1])

amount = int(input("Enter the amount in Rupees = "))
print("You want to convert Rupee to ? available option are = ")
[print(item) for item in dict.keys()]
currency = input("Enter valid option = ")

print(f"total amount after conversion is {amount * dict[currency]}")

        