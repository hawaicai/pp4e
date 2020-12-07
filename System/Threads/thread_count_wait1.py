"""
使用mutexes在父/子线程中探知线程何时结束，而不再使用
time.sleep；给stdout加锁以避免混杂在一起打印；
"""


import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutexes[myId].acquire()

for i in range(10):
    thread.start_new_thread(counter, (i, 100))
for mutex in exitmutexes:
    while not mutex.locked(): pass
print('Main thread exiting.')
