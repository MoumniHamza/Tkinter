from tkinter import *
from tkinter import ttk
root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert("", "1", "item1",text = "First Item")
treeview.insert("", "2", "item2",text = "Second Item")
treeview.insert("","end","item3",text = "Third Item")
treeview.insert("","end","item4",text = "Fourth Item")
image = PhotoImage(file = "python_logo.gif").subsample(10,10)
treeview.insert("item2", "end", "image", text = "Python3", image=image)
treeview.config( height = "5")
root.mainloop()