# -*-coding: utf-8-*-
# @Time  :2023/4/29 15:45
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections
from functools import cmp_to_key

class X:
    def test_explore(self):

        names1 = ["Mary", "John", "Emma"]
        heights1 = [180, 165, 170]
        l = list(zip(names1, heights1))

        l = sorted(l, key = lambda x: x[1], reverse=True)
        res = list(map(lambda x: x[0], l))
        return res


x = X()
x.test_explore()

