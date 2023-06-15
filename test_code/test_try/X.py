# encoding: utf-8
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections
import time


class X:
        def test_explore(self):
            s = ''
            for i in range(100000):
                s += str(i)
            return s



start = time.time()
x = X()
x.test_explore()
print(time.time() - start)