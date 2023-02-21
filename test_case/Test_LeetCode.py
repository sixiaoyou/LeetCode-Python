# -*-coding: utf-8-*-
# @Time  :2023/2/19 18:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: Test_LeetCode.py

'''
Note:
Test source_code/SourceCode_2023/February/LeetCode2037_MinimumNumberOfMovesToSeatEveryone
'''
from source_code.SourceCode_2023.February.LeetCode2037_MinimumNumberOfMovesToSeatEveryone import Solution


class Test_LeetCode(Solution):

    def setup(self):
        print("Initialize test...")

    def teardown(self):
        print("Clear test...")

    def test_solution(self):
        a = [12, 14, 19, 19, 12]
        b = [19, 2, 17, 20, 7]

        assert self.minMovesToSeat(a, b) == 19;
