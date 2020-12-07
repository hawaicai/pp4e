"""
找出单个目录下最大的python源代码文件。
搜索Windows Python源代码库，除非指定了dir命令行参数。
"""

import os
import glob
import sys
dirname = r'C:\Users\xia\AppData\Local\Programs\Python\Python36\Lib' if len(
    sys.argv) == 1 else sys.argv[1]

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
