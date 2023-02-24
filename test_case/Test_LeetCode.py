# -*-coding: utf-8-*-
# @Time  :2023/2/19 18:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: Test_LeetCode.py

'''
Note:
Test source_code/SourceCode_2023/February/LeetCode2485_FindThePivotInteger
'''

from source_code.SourceCode_2023.February.LeetCode2485_FindThePivotInteger import Solution


class Test_LeetCode(Solution):

    def setup(self):
        print("Initialize test...")

    def teardown(self):
        print("Clear test...")

    def test_solution(self):
        n = 49
        assert self.pivotIntegerV1(n) == 35
        assert self.pivotIntegerV2(n) == 35
        assert self.pivotIntegerV3(n) == 35
        assert self.pivotIntegerV4(n) == 35
        assert self.pivotIntegerV5(n) == 35
