# encoding: utf-8
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections
from collections import Counter
import time
import heapq

class X:
        def test_explore(self, nums):
           while nums:
               nums.remove(0)



nums = [0] * 20000000
start = time.time()
x = X()
x.test_explore(nums)
print(time.time() - start)