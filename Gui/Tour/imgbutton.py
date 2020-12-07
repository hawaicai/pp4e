gifdir = "../gifs/"
from tkinter import *

win = Tk()
img = PhotoImage(file=gifdir + "ora-pp.gif")
Button(win, image=img).pack()
win.mainloop()
