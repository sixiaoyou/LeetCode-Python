# encoding: utf-8
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections
from collections import Counter
import time
from collections import Counter


class X:
    def test_explore(self):
        a = set()
        a.add(1)
        a.add(2)
        a.add(3)
        b = set()
        b.add(10)
        a.remove(1)

a = X()
print(a.test_explore())










nums =  ["a", "a", "c", "d", "d", "d", "g", "o", "o"]

start = time.time()
x = X()
res = x.test_explore(nums)
print(res)
print(time.time() - start)
