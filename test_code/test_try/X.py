# -*-coding: utf-8-*-
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections
import time


class X:
        def test_explore(self, l):
            c1, c2 = 0, 0
            p = len(l)

            for j in l:
                if j != -1:
                    c1 += 1
                else:
                    c2 += 1

                if c1 == p:
                    p = j + 1
                    break

l = [0]
n = 82002
for i in range(n):
    l.append(-1)

x = X()
start = time.time()
print(x.test_explore(l))
print(time.time() - start)