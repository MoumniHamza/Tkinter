from tkinter import *
from tkinter import ttk

root = Tk()
myButton = ttk.Button(root , text = " Click me ")
myButton.pack()

def onclick():
    print('Clicked')
myButton.config(command = onclick)
logo = PhotoImage( file = 'python_logo.gif')
myButton.config(image = logo, compound = LEFT)
root.mainloop()