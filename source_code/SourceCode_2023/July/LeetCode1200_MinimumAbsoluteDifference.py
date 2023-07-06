# -*-coding: utf-8-*-
# @Time  :2023/7/5 15:15
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1200_MinimumAbsoluteDifference.py


'''
[1200. Minimum Absolute Difference]
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr


Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]


Constraints:

2 <= arr.length <= 105
-106 <= arr[i] <= 106
'''


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        ml = arr[:]

        for i in range(len(ml) - 1):
            ml[i] = ml[i + 1] - ml[i]

        mi = min(ml)
        res = []
        for j in range(len(ml) - 1):
            if ml[j] == mi:
                res.append([arr[j], arr[j + 1]])

        return res if res else [arr]

