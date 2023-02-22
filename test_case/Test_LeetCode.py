# -*-coding: utf-8-*-
# @Time  :2023/2/19 18:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: Test_LeetCode.py

'''
Note:
Test source_code/SourceCode_2023/February/LeetCode2553_SeparateTheDigitsInAnArray
'''

from source_code.SourceCode_2023.February.LeetCode2553_SeparateTheDigitsInAnArray import Solution


class Test_LeetCode(Solution):

    def setup(self):
        print("Initialize test...")

    def teardown(self):
        print("Clear test...")

    def test_solution(self):
        a = [13, 25, 83, 77]
        b = [1, 3, 2, 5, 8, 3, 7, 7]

        assert self.separateDigitsV1(a) == b
        assert self.separateDigitsV2(a) == b
