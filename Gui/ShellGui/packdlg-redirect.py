from tkinter import *
from packdlg import runPackDialog
import sys
sys.path.append("D:\svn\python")
from PP4E.Gui.Tools.guiStreams import redirectedGuiFunc


def runPackDialog_Wrapped():
    redirectedGuiFunc(runPackDialog)


if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=runPackDialog_Wrapped).pack(fill=X)
    root.mainloop()
