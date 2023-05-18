# -*-coding: utf-8-*-
# @Time  :2023/5/18 8:23
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2293_MinMaxGame.py


'''
[2293. Min Max Game]
You are given a 0-indexed integer array nums whose length is a power of 2.

Apply the following algorithm on nums:

Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the last number that remains in nums after applying the algorithm.



Example 1:


Input: nums = [1,3,5,2,4,8,2,2]
Output: 1
Explanation: The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.
Example 2:

Input: nums = [3]
Output: 3
Explanation: 3 is already the last remaining number, so we return 3.


Constraints:

1 <= nums.length <= 1024
1 <= nums[i] <= 109
nums.length is a power of 2.
'''
from typing import List


class SolutionV1:
    def minMaxGame(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 1:
            return (nums[0])
        elif l == 2:
            return min(nums)

        while l != 1:
            l = len(nums)

            if l == 1:
                return nums[0]

            i = 0
            while i < l:

                if i + 1 < l and nums[i] < nums[i + 1]:
                    nums[i + 1] = -1
                else:
                    nums[i] = -1

                if i + 3 < l and nums[i + 2] > nums[i + 3]:
                    nums[i + 3] = -1
                else:
                    if i + 2 < l:
                        nums[i + 2] = -1

                i += 4

            nums = list(filter(lambda x: x != -1, nums))


class SolutionV2:
    def minMaxGame(self, nums: List[int]) -> int:

        n = len(nums)

        while n != 1:
            m = n // 2
            for i in range(m):
                if i % 2 == 0:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])
            n = m
        return nums[0]

