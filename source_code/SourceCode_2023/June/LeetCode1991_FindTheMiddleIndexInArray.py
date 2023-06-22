# -*-coding: utf-8-*-
# @Time  :2023/6/22 6:19
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1991_FindTheMiddleIndexInArray.py

'''
[1991. Find the Middle Index in Array]
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.



Example 1:

Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
Example 2:

Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
Example 3:

Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.


Constraints:

1 <= nums.length <= 100
-1000 <= nums[i] <= 1000
'''
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        l = len(nums) - 1


        if l == 0:
            return 0
        elif len(set(nums)) == 1:
            return -1

        start, end = 0, l
        lsum, rsum, hsum = nums[start], nums[end], sum(nums) // 2

        while start < end:
            if rsum > hsum:
                rsum -= nums[end]
                while start + 1 <= end:
                    if start + 1 == end and lsum == 0:
                        return end

                    start += 1
                    lsum += nums[start]
                    if lsum == rsum:
                        return start + 1

            if lsum > hsum:
                 lsum -= nums[start]
                 while end - 1 > start:
                    end -= 1
                    rsum += nums[end]
                    if lsum == rsum:
                        return end + 1

            if lsum < rsum:
                start += 1
                lsum += nums[start]
            elif lsum > rsum:
                end -= 1
                rsum += nums[end]
            else:
                return start

        return -1

