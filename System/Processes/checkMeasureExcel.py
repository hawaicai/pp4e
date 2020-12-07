
import xlrd
import windnd
import tkinter
import exceltest
from tkinter.messagebox import *


def check1():
    try:
        checkfilename1 = txt1.get("0.0", "1.end")
        data1 = xlrd.open_workbook(checkfilename1)
        checkresult1 = exceltest.checkBegin(data1)
        message = "迭代1计划：" + str(checkresult1)
        return message
    except Exception as e:
        return "迭代1计划 error"


def check2():
    try:
        checkfilename2 = txt2.get("0.0", "1.end")
        data2 = xlrd.open_workbook(checkfilename2)
        checkresult2 = exceltest.checkSprint1(data2)
        message = "\n迭代1完成迭代2计划:" + str(checkresult2)
        return message
    except Exception as e:
        return "\n迭代1完成迭代2计划 error"


def check3():
    try:
        checkfilename3 = txt3.get("0.0", "1.end")
        data3 = xlrd.open_workbook(checkfilename3)
        checkresult3 = exceltest.checkSprint2(data3)
        message = "\n迭代2完成:" + str(checkresult3)
        return message
    except Exception as e:
        return "\n迭代2完成 error"


def check4():
    try:
        checkfilename4 = txt4.get("0.0", "1.end")
        data4 = xlrd.open_workbook(checkfilename4)
        checkresult4 = exceltest.checkEnd(data4)
        message = "\n迭代结束:" + str(checkresult4)
        return message
#        showinfo("check", message)
    except Exception as e:
        return "\n迭代结束 error"


def check():
    checkresult1 = check1()
    checkresult2 = check2()
    checkresult3 = check3()
    checkresult4 = check4()
    msg = "check result:\n" + checkresult1 + \
        checkresult2 + checkresult3 + checkresult4
    showinfo("check", msg)


root = tkinter.Tk()                     # 创建窗口对象的背景色
#
label1 = tkinter.Label(root, text="迭代1计划")
label1.pack()
txt1 = tkinter.Text(root, height=2, width=100)


def func(ls):
    txt1.delete(0., "end")
    for i in ls:
        txt1.insert("end", i.decode("gbk") + '\n')


# windows 挂钩
windnd.hook_dropfiles(txt1.winfo_id(), func)
txt1.pack()

label2 = tkinter.Label(root, text="迭代1完成迭代2计划")
label2.pack()
txt2 = tkinter.Text(root, height=2, width=100)


def func2(ls):
    txt2.delete(0., "end")
    for i in ls:
        txt2.insert("end", i.decode("gbk") + '\n')


# windows 挂钩
windnd.hook_dropfiles(txt2.winfo_id(), func2)
txt2.pack()

label3 = tkinter.Label(root, text="迭代2完成")
label3.pack()
txt3 = tkinter.Text(root, height=2, width=100)


def func3(ls):
    txt3.delete(0., "end")
    for i in ls:
        txt3.insert("end", i.decode("gbk") + '\n')


# windows 挂钩
windnd.hook_dropfiles(txt3.winfo_id(), func3)
txt3.pack()

label4 = tkinter.Label(root, text="迭代结束")
label4.pack()
txt4 = tkinter.Text(root, height=2, width=100)


def func4(ls):
    txt4.delete(0., "end")
    for i in ls:
        txt4.insert("end", i.decode("gbk") + '\n')


# windows 挂钩
windnd.hook_dropfiles(txt4.winfo_id(), func4)
txt4.pack()

button = tkinter.Button(root, text="check", command=check)
button.pack()
root.mainloop()
