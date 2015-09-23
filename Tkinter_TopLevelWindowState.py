from tkinter import *
from tkinter import ttk

root = Tk()
window = Toplevel(root)
window.title('New window')
#Lower the window
window.lower()
#makes the root window as the first window
window.lift(root)
#makes the window in its maximum size
window.state('zoomed')
#makes the window iconic
window.state('iconic')
# It gives a width and a length plus an x and y position
window.geometry('600*500+100+100')
root.mainloop()