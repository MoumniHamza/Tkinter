from tkinter import *

root = Tk()
display = Text(root, width = 20 , height = 10)
display.pack()
display.insert('1.0' , 'this is my string')
#Adding a tag
display.tag_add( 'my_tag','1.0','1.3')
display.tag_config('my_tag', background = 'blue')
display.mark_names()
root.mainloop()