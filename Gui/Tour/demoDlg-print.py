"""
与之类似，会显示出对话调用后的返回值；lambda表达式保存局部域内的数据，再传递给处理器（按钮按下处理器
通常不含参数，同时，封闭范围内引起对循环变量不起作用），工作机制就像内嵌的def函数声明：def fun(key=key):self.printit(key)
"""

from tkinter import *
from dialogTable import demos
from quitter import Quitter


class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Basic demos").pack()
        for key in demos:
            func = (lambda key=key: self.printit(key))
            Button(self, text=key, command=func).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

    def printit(self, name):
        print(name, 'returns=>', demos[name]())


if __name__ == '__main__':
    Demo().mainloop()
