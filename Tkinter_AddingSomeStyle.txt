from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text ="Hello my name is Hamza welcome to this tkinter tutorial")
label.pack()
label.config(wrap = 100)
label.config(foreground ='white' , background ='black')
label.config(font = ('arial', 12 ,'bold'))
root.mainloop()
