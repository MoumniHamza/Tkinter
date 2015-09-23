from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)
frame.config( height = 300 , width = 400)
frame.config(relief = RAISED)
ttk.Button(frame, text = 'I am a button' ).grid()
ttk.LabelFrame(height =300, width =400,text = 'I am a LabelFrame').pack()
frame.pack()
root.mainloop()