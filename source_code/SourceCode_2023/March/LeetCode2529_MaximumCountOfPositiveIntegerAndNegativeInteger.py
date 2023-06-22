# -*-coding: utf-8-*-
# @Time  :2023/3/4 18:43
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2529_MaximumCountOfPositiveIntegerAndNegativeInteger.py

'''
[LeetCode2529. Maximum Count of Positive Integer and Negative Integer]
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.



Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.


Constraints:

1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.


Follow up: Can you solve the problem in O(log(n)) time complexity?
'''

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
            if nums[0] > 0 or nums[-1] < 0:
                return len(nums)

            p, n, l = 0, 0, len(nums) - 1
            start, end = 0, l
            while start <= end:
                mid = (start + end) // 2

                if nums[mid] < 0:
                    if nums[mid+1] > 0:
                        p, n = len(nums[mid+1:]), len(nums[:mid+1])
                        return max(p, n)
                    else:
                        start = mid + 1
                elif nums[mid] > 0:
                    if nums[mid-1]<0:
                        p, n = len(nums[mid:]), len(nums[:mid])
                        return max(p, n)
                    else:
                        end = mid - 1
                else:
                    left, right = mid, mid
                    while left > -1 and nums[left] == 0:
                            left -= 1

                    while right <= l and nums[right] == 0:
                            right += 1

                    p, n = len(nums[right:]), len(nums[:left+1])
                    return max(p, n)

            return max(p, n)
