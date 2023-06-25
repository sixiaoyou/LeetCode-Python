# -*-coding: utf-8-*-
# @Time  :2023/6/26 7:03
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2475_NumberOfUnequalTripletsInArray.py


'''
[2475. Number of Unequal Triplets in Array]
You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.



Example 1:

Input: nums = [4,4,2,4,3]
Output: 3
Explanation: The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: No triplets meet the conditions so we return 0.


Constraints:

3 <= nums.length <= 100
1 <= nums[i] <= 1000
'''
from collections import Counter


class SolutionV1:
    def unequalTriplets(self, nums: List[int]) -> int:

        l = len(nums)
        count = 0

        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        count += 1
        return count


class SolutionV2:
    def unequalTriplets(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        i = j = 0
        while i < n:
            while j < n and nums[j] == nums[i]:
                j += 1
            res += i * (j - i) * (n - j)
            i = j
        return res


class SolutionV3:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        n = len(nums)
        t = 0
        for v in count.values():
            res += t * v * (n - t - v)
            t += v
        return res

