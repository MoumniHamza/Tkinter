from tkinter import *
from tkinter import ttk

root = Tk()
progress = ttk.Progressbar(root , orient = HORIZONTAL, length = 200)
progress.pack()
progress.config( value = 4.5 , mode ='determinate', max = 11)
scale = ttk.Scale(root, orient = HORIZONTAL , length = 400)
scale.pack()
root.mainloop()
