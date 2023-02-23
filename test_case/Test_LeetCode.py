# -*-coding: utf-8-*-
# @Time  :2023/2/19 18:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: Test_LeetCode.py

'''
Note:
Test source_code/SourceCode_2023/February/LeetCode2220_MinimumBitFlipsToConvertNumber
'''

from source_code.SourceCode_2023.February.LeetCode2220_MinimumBitFlipsToConvertNumber import Solution


class Test_LeetCode(Solution):

    def setup(self):
        print("Initialize test...")

    def teardown(self):
        print("Clear test...")

    def test_solution(self):
        start, goal = 10, 7
        assert self.minBitFlipsV1(start, goal) == 3
        assert self.minBitFlipsV2(start, goal) == 3
        assert self.minBitFlipsV3(start, goal) == 3
