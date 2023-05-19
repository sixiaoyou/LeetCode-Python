# -*-coding: utf-8-*-
# @Time  :2023/5/19 10:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1085_SumOfDigitsInTheMinimumNumber.py

'''
[1085. Sum of Digits in the Minimum Number]
Given an integer array nums, return 0 if the sum of the digits of the minimum integer in nums is odd, or 1 otherwise.



Example 1:

Input: nums = [34,23,1,24,75,33,54,8]
Output: 0
Explanation: The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.
Example 2:

Input: nums = [99,77,33,66,55]
Output: 1
Explanation: The minimal element is 33, and the sum of those digits is 3 + 3 = 6 which is even, so the answer is 1.


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''
from typing import List


class SolutionV1:
    def sumOfDigits(self, nums: List[int]) -> int:
        return 1 if sum(map(lambda x: int(x), list(str(min(nums))))) % 2 == 0 else 0

class SolutionV2:
    def sumOfDigits(self, nums: List[int]) -> int:
        mi = min(nums)
        s = 0
        for i in str(mi):
            s += int(i)

        return 1 if s % 2 == 0 else 0