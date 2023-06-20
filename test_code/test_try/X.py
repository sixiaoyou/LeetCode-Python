# encoding: utf-8
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py


import collections
import time
import heapq

from collections import defaultdict
class X:
        def test_explore(self, n):
            s = "cba"
            s = sorted(s, key = lambda x: ord(x))
            print(s)


n = 500
start = time.time()
x = X()
x.test_explore(n)
print(time.time() - start)