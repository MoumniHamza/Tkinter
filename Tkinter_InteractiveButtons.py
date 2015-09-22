from tkinter import *
from tkinter import ttk

class Helloapp:
       def __init__(self,master):
           self.label = ttk.Label(master , text ="Hello Everyone")
           self.label.grid(row =0, column =0, columnspan =2)

           ttk.Button(master, text = 'Oregon', command = self.Oregon).grid(row =1 , column =0)
           ttk.Button(master, text = 'California', command = self.California).grid(row =1 , column =1)
       def Oregon(self):
           self.label.config( text = 'Welcome to Oregon')
       def California(self):
           self.label.config( text = 'Welcome to California')
def main():
    root= Tk()
    app = Helloapp(root)
    root.mainloop()
if __name__== "__main__":main()