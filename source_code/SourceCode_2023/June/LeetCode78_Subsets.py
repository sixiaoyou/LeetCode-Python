# -*-coding: utf-8-*-
# @Time  :2023/6/28 14:44
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode78_Subsets.py


'''
[78. Subsets]
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''
import copy
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        self.backtracking(res, path, nums, 0)
        return res

    def backtracking(self, res, path, nums, startIndex):
        res.append(path)

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(res, path, nums, i + 1)
            path.pop()
