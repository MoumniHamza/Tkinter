from tkinter import *
from tkinter import ttk

root = Tk()
month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))
year = StringVar()
spinbox = Spinbox(root , from_ = 1990 , to = 2020, textvariable = year)
spinbox.pack()
root.mainloop()
