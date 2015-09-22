from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text ="Hello my name is Hamza welcome to this tkinter tutorial")
label.pack()
label.config(foreground ='black')
label.config(font = ('arial',15, 'bold'))
PhotoImage(file ="python_logo.gif")
logo =PhotoImage(file ="python_logo.gif")
label.config(image = logo)
label.config(compound = LEFT)
root.mainloop()
