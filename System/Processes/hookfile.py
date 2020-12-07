
import windnd
import tkinter

top = tkinter.Tk()

txt = tkinter.Text(top)

# 对文件的操作


def func(ls):
    txt.delete(0., "end")
    for i in ls:
        txt.insert("end", i.decode("gbk") + '\n')


def check():
    print(txt.get("0.0", "end"))


# windows 挂钩
windnd.hook_dropfiles(txt.winfo_id(), func)
txt.pack(side="top")
botton = tkinter.Button(text="check", command=check)
botton.pack()
top.mainloop()
