# -*-coding: utf-8-*-
# @Time  :2023/4/29 15:23
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: test_data.py
import collections


class Test_Data:

    def GenTestData(self):
        t1 = [-1,0,3,5,9,12]
        t2 = [-1,0,3,5,9,12]
        t3 = [5]
        t4 = [-1,0,3,5,9,12]

        l1 = [t1, 9]
        l2 = [t2, 2]
        l3 = [t3, 5]
        l4 = [t4, 0]

        t = [l1, l2, l3, l4]
        # t = [t3]
        return t

a = Test_Data()
print(a.GenTestData())
