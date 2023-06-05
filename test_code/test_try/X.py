# -*-coding: utf-8-*-
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections


class X:
        def test_explore(self):
            d = collections.defaultdict(list)
            for i,j in [[1,2],[1,0],[1,3]]:
                d[i].append(j)
            print(d)



x = X()
print(x.test_explore())
