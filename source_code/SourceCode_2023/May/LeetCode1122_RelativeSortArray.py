# -*-coding: utf-8-*-
# @Time  :2023/5/6 22:19
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1122_RelativeSortArray.py

'''
[1122. Relative Sort Array]
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]


Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
'''

class SolutionV1:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        d1, d2 = {}, {}

        for i in range(len(arr2)):
            d1[arr2[i]] = i
            d2[i] = 0

        for j in arr1:
            if j in d1:
                d2[d1[j]] += 1
            else:
                res.append(j)

        res.sort()
        ans = []
        for k in range(len(arr2)):
            ans += [arr2[k]] * d2[k]

        return ans + res

class SolutionV2:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x: int) -> (int, int):
            return rank[x] if x in rank else x

        l = len(arr2)
        rank = {x: i - l for i, x in enumerate(arr2)}

        arr1.sort(key=mycmp)
        return arr1

