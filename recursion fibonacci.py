def fibo(n):
    if n==0:
        return 0
    
    elif n==1:
        return 1
    
    else:
        return (fibo(n-1)+fibo(n-2))



num = int(input("Enter the number = "))

if num == 1:
    print("0")
else:
    for x in range(0,num):
      print(fibo(x))