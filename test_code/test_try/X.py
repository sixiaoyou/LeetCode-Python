# -*-coding: utf-8-*-
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections


class X:
        def test_explore(self):
            ls, res = ["abjfedid"],[]
            for i in ls:
                res.append(sum(map(lambda x: ord(x) - 97, list(i))))
            print(res)



x = X()
print(x.test_explore())
