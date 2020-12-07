"""
PyDraw 1.1
"""

helpstr = """--PyDraw 1.1 版本
鼠标命令：
	左键				= 设置目标点
	左键 + 移动		= 绘制新的对象
	双击左键			= 清除所有对象
	右键				= 移动当前对象
	中间				= 选择最近的对象
	中间 + 移动 		= 拖拽当前的对象

键盘命令：
w= 选择边框宽度		c= 选择颜色
u= 选择移动单元		s= 选择移动延迟
o= 画椭圆			r= 画长方形
l= 画直线			a= 画弧
d= 删除对象			1= 增加对象
2= 减少对象			f= 填充对象
b= 填充背景			p= 增加图片
z= 保存附言			x= 选择钢笔模式
？= 帮助				other= 清除文本
"""

import time
import sys
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
PicDir = '../gifs'

if sys.platform[:3] == 'win':
    HelpFont = ('courier', 9, 'normal')
else:
    HelpFont = ('courier', 12, 'normal')

pickDelays = [0.01, 0.025, 0.05, 0.10, 0.25, 0.0, 0.001, 0.005]
pickUnits = [1, 2, 4, 6, 8, 10, 12]
pickWidths = [1, 2, 5, 10, 20]
pickFills = [None, 'white', 'blue', 'red',
             'black', 'yellow', 'green', 'purple']
pickPens = ['elastic', 'scribble', 'trails']


class MovingPics:
    def __init__(self, parent=None):
        canvas = Canvas(parent, width=500, height=500, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        canvas.bind('<ButtonPress-1>', self.onStart)
        canvas.bind('<B1-Motion>', self.onGrow)
        canvas.bind('<Double-1>', self.onClear)
        canvas.bind('<ButtonPress-3>', self.onMove)
        canvas.bind('<Button-2>', self.onSelect)
        canvas.bind('<B2-Motion>', self.onDrag)
        parent.bind('<KeyPress>', self.onOptions)
        self.createMethod = Canvas.create_oval
        self.canvas = canvas
        self.moving = []
        self.images = []
        self.object = None
        self.where = None
        self.scribbleMode = 0
        parent.title('PyDraw - Moving Pictures 1.1')
        parent.protocol('WM_DELETE_WINDOW', self.onQuit)
        self.realquit = parent.quit
        self.textInfo = self.canvas.create_text(
            5, 5, anchor=NW, font=HelpFont, text='Press ? for help')

    def onStart(self, event):
        self.where = event
        self.object = None

    def onGrow(self, event):
        canvas = event.widget
        if self.object and pickPens[0] == 'elastic':
            canvas.delete(self.object)
        self.object = self.createMethod(canvas,
                                        self.where.x, self.where.y,
                                        event.x, event.y,
                                        fill=pickFills[0], width=pickWidths[0])
        if pickPens[0] == 'scribble':
            self.where = event

    def onClear(self, event):
        if self.moving:
            return
        event.widget.delete('all')
        self.images = []
        self.textInfo = self.canvas.create_text(5, 5, anchor=NW,
                                                font=HelpFont, text='Press ? for help')

    def plotMoves(self, event):
        diffX = event.x - self.where.x
        diffY = event.y = self.where.y
        reptX = abs(diffX) // pickUnits[0]
        reptY = abs(diffY) // pickUnits[0]
        incrX = pickUnits[0] * ((diffX > 0) or -1)
        incrY = pickUnits[0] * ((diffY > 0) or -1)
        return incrX, reptX, incrY, reptY

    def onMove(self, event):
        traceEvent('onMove', event, 0)
        object = self.object
        if object and object not in self.moving:
            msecs = int(pickDelays[0] * 1000)
            parms = 'Delay=%d msec, Units=%d' % (msecs, pickUnits[0])
            self.setTextInfo(parms)
            self.moving.append(object)
            canvas = event.widget
            incrX, reptX, incrY, reptY = self.plotMoves(event)
            for i in range(reptX):
                canvas.move(object, incrX, 0)
                canvas.update()
                time.sleep(pickDelays[0])
            for i in range(reptY):
                canvas.move(object, 0, incrY)
                canvas.update()
                time.sleep(pickDelays[0])
            self.moving.remove(object)
            if self.object == object:
                self.where = event

    def onSelect(self, event):
        self.where = event
        self.object = self.canvas.find_closest(event.x, event.y)[0]

    def onDrag(self, event):
        diffX = event.x - self.where.x
        diffY = event.y = self.where.y
        self.canvas.move(self.object, diffX, diffY)
        self.where = event

    def onOptions(self, event):
        keymap = {
            'w': lambda self: self.changeOption(pickWidths, 'Pen Width'),
            'c': lambda self: self.changeOption(pickFills, 'Color'),
            'u': lambda self: self.changeOption(pickUnits, 'Move Unit'),
            's': lambda self: self.changeOption(pickDelays, 'Move Delay'),
            'x': lambda self: self.changeOption(pickPens, 'Pen Mode'),
            'o': lambda self: self.changeDraw(Canvas.create_oval, 'Oval'),
            'r': lambda self: self.changeDraw(Canvas.create_rectangle, 'Rectangle'),
            'l': lambda self: self.changeDraw(Canvas.create_line, 'Line'),
            'a': lambda self: self.changeDraw(Canvas.create_arc, 'Arc'),
            'd': MovingPics.deleteObject,
            '1': MovingPics.raiseObject,
            '2': MovingPics.lowerObject,
            'f': MovingPics.fillObject,
            'b': MovingPics.fillBackground,
            'p': MovingPics.addPhotoItem,
            'z': MovingPics.savePostscript,
            '?': MovingPics.help
        }
        try:
            keymap[event.char](self)
        except KeyError:
            self.setTextInfo('Press ? for help')

    def changeDraw(self, method, name):
        self.createMethod = method
        self.setTextInfo('Draw Object=' + name)

    def changeOption(self, list, name):
        list.append(list[0])
        del list[0]
        self.setTextInfo('%s=%s' % (name, list[0]))

    def deleteObject(self):
        if self.object != self.textInfo:
            self.canvas.delete(self.object)
            self.object = None

    def raiseObject(self):
        if self.object:
            self.canvas.tkraise(self.object)

    def lowerObject(self):
        if self.object:
            self.canvas.lower(self.object)

    def fillObject(self):
        if self.object:
            type = self.canvas.type(self.object)
            if type == 'image':
                pass
            elif type == 'text':
                self.canvas.itemconfig(self.object, fill=pickFills[0])
            else:
                self.canvas.itemconfig(
                    self.object, fill=pickFills[0], width=pickWidths[0])

    def fillBackground(self):
        self.canvas.config(bg=pickFills[0])

    def addPhotoItem(self):
        if not self.where:
            return
        filetypes = [('Gif files', '.gif'), ('All files', '*')]
        file = askopenfilename(initialdir=PicDir, filetypes=filetypes)
        if file:
            image = PhotoImage(file=file)
            self.images.append(image)
            self.object = self.canvas.create_image(
                self.where.x, self.where.y, image=image, anchor=NW)

    def savePostscript(self):
        file = asksaveasfilename()
        if file:
            self.canvas.postscript(file=file)

    def help(self):
        self.setTextInfo(helpstr)
        #showinfo('PyDraw', helpstr)

    def setTextInfo(self, text):
        self.canvas.dchars(self.textInfo, 0, END)
        self.canvas.insert(self.textInfo, 0, text)
        self.canvas.tkraise(self.textInfo)

    def onQuit(self):
        if self.moving:
            self.setTextInfo("Can't quit while move in progress")
        else:
            self.realquit()


def traceEvent(label, event, fullTrace=True):
    print(label)
    if fullTrace:
        for attr in dir(event):
            if attr[:2] != '  ':
                print(attr, '=>', getattr(event, attr))


if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        PicDir = argv[1]
    root = Tk()
    MovingPics(root)
    root.mainloop()
