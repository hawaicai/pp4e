import os

import tkinter.filedialog


def openfilename():
    default_dir = r"C:\Users\lenovo\Desktop"  # 设置默认打开目录f
    fname = tkinter.filedialog.askopenfilename(
        title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
    print(fname)
    return fname
