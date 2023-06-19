# -*-coding: utf-8-*-
# @Time  :2023/5/11 8:03
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2418_SortThePeople.py

'''
[2418. Sort the People]
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.



Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.


Constraints:

n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
'''

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = list(zip(names, heights))

        l = sorted(l, key = lambda x: x[1], reverse=True)
        res = list(map(lambda x: x[0], l))
        return res
