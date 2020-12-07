"""
找出整个目录树中最大的Python源代码文件。
搜索Python源代码库，利用pprint漂亮地显示结果。
"""

import sys
import os
import pprint
trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Users\xia\AppData\Local\Programs\Python\Python36\Lib'
else:
    dirname = '/usr/lib/python'

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace:
        print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace:
                print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
