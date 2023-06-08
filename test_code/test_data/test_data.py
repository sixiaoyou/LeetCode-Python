# -*-coding: utf-8-*-
# @Time  :2023/4/29 15:23
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: test_data.py
import collections


class Test_Data:

    def GenTestData(self):
        t1 = ['j', 'j', 'bi']
        t2 = ["c", "abjfedid", "gghdijjf"]
        t3 = ["h","fhjfdghj","fhjfdgig"]
        t4 = [3,[[0,1],[0,2],[2,1],[1,2],[1,0],[2,0]],5]
        t5 =  [3,[[2, 0], [0, 1], [1, 2], [1, 0], [2, 1], [0, 2]],3]
        t = [t1, t2, t3, t4, t5]
        t = [t1, t2, t3]
        return t
