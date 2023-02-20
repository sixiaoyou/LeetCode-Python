# -*-coding: utf-8-*-
# @Time  :2023/2/19 18:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: Test_LeetCode.py

from ..source_code.LeetCode2520_CountTheDigitsThatDivideANumber import Solution


class Test_LeetCode(Solution):

    def setup(self):
        print("Initialize test...")

    def teardown(self):
        print("Clear test...")

    def test_solution(self):
        num = 121
        assert self.countDigitsV1(num) == 2;
        assert self.countDigitsV2(num) == 2;
