# -*-coding: utf-8-*-
# @Time  :2023/2/19 18:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: Test_LeetCode.py

from ..source_code.LeetCode2535_DifferenceBetweenElementSumAndDigitSumOfAnArray import Solution


class Test_LeetCode(Solution):

    def setup(self):
        print("Initialize test...")

    def teardown(self):
        print("Clear test...")

    def test_solution(self):
        nums = [1, 15, 6, 3]
        assert self.differenceOfSumV1(nums) == 9;
        assert self.differenceOfSumV2(nums) == 9;