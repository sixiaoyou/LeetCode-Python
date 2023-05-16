# -*-coding: utf-8-*-
# @Time  :2023/4/29 15:23
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: test_data.py
import collections


class Test_Data:

    def GenTestData(self):
        t1 = [[3,7,8],[9,11,13],[15,16,17]]
        t2 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
        t3 = [[7,8],[1,2]]
        t4 = [[3,6],[7,1],[5,2],[4,8]]
        t5 = [[54275,58407,32176,89233],[36006,18811,80905,68401],[23392,15661,35000,59735]]

        print(list(zip(*t4)))


        t = [t1, t2, t3, t4, t5]
        # t = [t3]
        # return t

a = Test_Data()
print(a.GenTestData())
