from tkinter import *
from tkinter.messagebox import *


def notdone():
    showerror('Not implemented', 'Not yet available')


def makemenu(parent):
    menubar = Frame(parent)
    menubar.pack(side=TOP, fill=X)

    fButton = Menubutton(menubar, text='File', underline=0)
    fButton.pack(side=LEFT)
    file = Menu(fButton)
    file.add_command(label='New...', command=notdone, underline=0)
    file.add_command(label='Open...', command=notdone, underline=0)
    file.add_command(label='Quit', command=parent.quit, underline=0)
    fButton.config(menu=file)

    eButton = Menubutton(menubar, text='Edit', underline=0)
    eButton.pack(side=LEFT)
    edit = Menu(eButton, tearoff=False)
    edit.add_command(label='Cut', command=notdone, underline=0)
    edit.add_command(label='Paste', command=notdone, underline=0)
    edit.add_separator()
    eButton.config(menu=edit)

    submenu = Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=parent.quit, underline=0)
    submenu.add_command(label='Eggs', command=notdone, underline=0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)
    return menubar


if __name__ == '__main__':
    root = Tk()
    root.title('menu_frm')
    makemenu(root)
    msg = Label(root, text='Frame menu basics')
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()
