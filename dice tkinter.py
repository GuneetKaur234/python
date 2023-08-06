from tkinter import *
from PIL import ImageTk, Image  
import random

root = Tk()
root.geometry("300x300")
root.title("Dice simulator")
root.config(bg ='#129AB9')
root.resizable(0,0)

dice = [".vscode\python\dice1.png",".vscode\python\dice2.jpg",".vscode\python\dice3.png",".vscode\python\dice4.jpg",".vscode\python\dice5.png",".vscode\python\dice6.png"]

a = random.choice(dice)
image =  ImageTk.PhotoImage(Image.open(a))




frame1 = Frame(root)
frame1.pack()

Lab_image= Label(root,image=image)
Lab_image.image = image
Lab_image.place(x=250,y=100)
Lab_image.pack()

def play():
    a = random.choice(dice)
    image =  ImageTk.PhotoImage(Image.open(a))
    Lab_image.configure(image=image)
    Lab_image.image = image


button1 = Button(root, text = " Let's Roll ",relief=RAISED,borderwidth=5,bg="yellow",command= play)
button1.place(x=200,y=250,width= 90,height=40)


























root.mainloop()