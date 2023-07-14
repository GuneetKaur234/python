# a = lambda x : (x+2)*3
# b = lambda x : x*x*x

# def myfunct(n1,n2,v1,v2):
#     if n1(v1) > n2(v2):
#         return 1
#     else:
#         return 0

# print(myfunct(n1=a,n2=b,v1=3,v2=2))

myfunct = lambda x,y :  print(f"{x} X {y} = {x*y}") #if x >y  else print(f"{x}")

print(myfunct(2,3))