# -*-coding: utf-8-*-
# @Time  :2023/4/29 15:23
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: test_data.py
import collections


class Test_Data:

    def GenTestData(self):
        names1 =  ["Mary","John","Emma"]
        heights1 = [180,165,170]

        names2 = ["Alice","Bob","Bob"]
        heights2 = [155,185,150]

        l1 = [names1, heights1]
        l2 = [names2, heights2]

        l = [l1, l2]

        return l