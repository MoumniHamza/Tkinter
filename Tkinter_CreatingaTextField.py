from tkinter import *

root = Tk()
display = Text(root, width = 20 , height = 10)
display.pack()
display.insert('1.0','end', ' this is my string')
root.mainloop()