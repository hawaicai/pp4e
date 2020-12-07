#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-24 11:20:41
# @Author  : hawaicai (hawaicai@163.com)
# @Link    : http://hawaicai.org
# @Version : $Id$

import os
import time
import sys

mypid = os.getpid()
parentpid = os.getppid()
sys.stderr.write('Child %d of %d got arg: "%s"\n' %
                 (mypid, parentpid, sys.argv[1]))

for i in range(2):
    time.sleep(3)
    recv = input()
    time.sleep(3)
    send = 'Child %d got: [%s]' % (mypid, recv)
    print(send)
    sys.stdout.flush()
