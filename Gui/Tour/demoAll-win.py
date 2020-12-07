from tkinter import *
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']


def makePopups(modnames):
    demoObjects = []
    for modename in modnames:
        module = __import__(modename)
        window = Toplevel()
        demo = module.Demo(window)
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects


def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()


root = Tk()
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple Toplevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()
