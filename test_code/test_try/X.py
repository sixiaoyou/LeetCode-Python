# -*-coding: utf-8-*-
# @Time  :2023/4/29 15:45
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections
from functools import cmp_to_key

class X:
    def cmp(self, rank, arr1):
         arr1[rank[x]] = x if x in arr1 else rank[x]

    def test_explore(self):

        a = [1,2,3]
        b = [2,3,1]

        l = len(b)
        rank = {x: i - l for i, x in enumerate(b)}
        print(rank)
        a.sort(key = self.cmp(rank, a))
        print(a)

x = X()
x.test_explore()

