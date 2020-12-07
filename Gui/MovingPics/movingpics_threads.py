import _thread as thread
import time
import sys
import random
from tkinter import Tk, mainloop
from movingpics import MovingPics, pickUnits, pickDelays


class MovingPicsThreaded(MovingPics):
    def __init__(self, parent=None):
        MovingPics.__init__(self, parent)
        self.mutex = thread.allocate_lock()

    def onMove(self, event):
        object = self.object
        if object and object not in self.moving:
            msecs = int(pickDelays[0] * 1000)
            parms = 'Delay=%d msec, Units=%d' % (msecs, pickUnits[0])
            self.setTextInfo(parms)
            self.moving.append(object)
            thread.start_new_thread(self.doMove, (object, event))

    def doMove(self, object, event):
        canvas = event.widget
        incrX, reptX, incrY, reptY = self.plotMoves(event)
        for i in range(reptX):
            canvas.move(object, incrX, 0)
            time.sleep(pickDelays[0])
        for i in range(reptY):
            canvas.move(object, 0, incrY)
            time.sleep(pickDelays[0])
        self.moving.remove(object)
        if self.object == object:
            self.where = event


if __name__ == '__main__':
    root = Tk()
    MovingPicsThreaded(root)
    root.mainloop()
