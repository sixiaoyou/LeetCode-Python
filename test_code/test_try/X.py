# -*-coding: utf-8-*-
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py


class X:
        def test_explore(self):
            l1 = [1, 2, 3]
            l2 = [4, 5, 6]

            for i,j in zip(l1, l2):
                print(i, j)

x = X()
print(x.test_explore())
