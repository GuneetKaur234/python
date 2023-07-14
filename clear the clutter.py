import os

# os.chdir("D:\guneet\study\python\clear the clutter")
# print(os.getcwd())

# os.mkdir("D:\guneet\study\python\clear the clutter")
# print("file created")


# for x in range (0,9):
#     os.chdir("D:\guneet\study\python\clear the clutter")
#     f= open(f"hello{x}.png", "x")
#     print("files created")

for x in range (0,9):
    os.chdir("D:\guneet\study\python\clear the clutter")
    os.rename(f"hello{x}.png", f"guneet{x}.png")
    print("files created")