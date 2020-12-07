"""
线程基本操作：并行地启用5个函数副本；利用time.sleep避免主线程
过早退出，这样在某些系统平台上将导致其他线程中止；共享stdout；
线程输出在这个版本里可能随机混合在一起。
"""

import _thread as thread,time

def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (myId, i))

for i in range(5):
    thread.start_new_thread(counter, (i, 5))
time.sleep(6)
print('Main thread exiting.')
