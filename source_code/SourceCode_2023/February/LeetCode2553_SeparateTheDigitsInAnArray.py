# -*-coding: utf-8-*-
# @Time  :2023/2/22 16:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2553_SeparateTheDigitsInAnArray.py

'''
[LeetCode2553. Separate the Digits in an Array]
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].


Example 1:

Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation:
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
Example 2:

Input: nums = [7,1,3,9]
Output: [7,1,3,9]
Explanation: The separation of each integer in nums is itself.
answer = [7,1,3,9].


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
'''


from typing import List


class Solution:

    def get_resultV1(self, nums):
        return list(map(lambda x: int(x), "".join(list(map(lambda y: str(y), nums)))))

    def get_resultV2(self, nums):
        sn = ''.join(map(lambda x: str(x), nums))
        rn = []
        for r in sn:
            rn.append(int(r))
        return rn

    def separateDigitsV1(self, nums: List[int]) -> List[int]:
        return self.get_resultV1(nums)

    def separateDigitsV2(self, nums: List[int]) -> List[int]:
        return self.get_resultV2(nums)
