from tkinter import *
from tkinter import ttk

root = Tk()
RadioButton = ttk.Radiobutton(root , text = 'Breakfast').pack()
ttk.Checkbutton(root, text = ' sausage').pack()
ttk.Checkbutton(root, text = ' milk').pack()
ttk.Checkbutton(root, text = ' eggs').pack()
ttk.Checkbutton(root, text = ' pancake').pack()
ttk.Checkbutton(root, text = ' cheese').pack()
root.mainloop()