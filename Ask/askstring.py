from tkinter.simpledialog import askstring
from tkinter import *

top = Tk()

top.geometry("100x100")
def show():
   name = askstring("Input", "Enter you name")
   print(name)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()