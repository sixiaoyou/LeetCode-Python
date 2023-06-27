# encoding: utf-8
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections
from collections import Counter
import time
import heapq
from queue import PriorityQueue


class X:
    def test_explore(self, nums):
        pass
nums = [1, 2, 3]
expect = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
start = time.time()
x = X()
res = x.test_explore(nums)
print(res == expect)
print(time.time() - start)
