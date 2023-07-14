Heights = input("Enter the list of Height seperated by space = ")

split_height = Heights.split(' ')

count = 0

for i in split_height:
    count = count + 1

for x in range(0,count):
    split_height[x] = int(split_height[x])

sum = 0 

for y in range(0,count):
    sum += split_height[x]

avg = round(sum/count)



print(f"Average of your heights is {avg}")

    