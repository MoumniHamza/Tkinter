from tkinter import *
from tkinter import ttk

root = Tk()
notebook = ttk.Notebook( root)
notebook.pack()
frame1= ttk.Frame(notebook)
frame2= ttk.Frame(notebook)
notebook.add(frame1 , text = 'one')
notebook.add(frame2, text = 'two')
root.mainloop()