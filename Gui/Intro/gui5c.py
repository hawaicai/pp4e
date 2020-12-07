from tkinter import *


class ThemedButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(fg='red', bg='black', font=(
            'courier', 12), relief=RAISED, bd=5)


B1 = ThemedButton(text='spam')
B2 = ThemedButton(text='eggs')
B2.pack(expand=YES, fill=BOTH)
B2.mainloop()
