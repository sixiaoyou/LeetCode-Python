# -*-coding: utf-8-*-
# @Time  :2023/4/29 15:45
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import time

import numpy


class X:
    def test_explore(self):
        l = []
        for i in range(5000000):
            l.append(-1)
        l.append(0)
        for j in range(5000000):
            l.append(-1)

        start = time.time()
        # l = list(filter(lambda x: x!=-1, l))
        for j in range(10000000):
            l.remove(-1)
        print(time.time() - start)
        return l



x = X()
print(x.test_explore())
