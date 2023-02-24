# -*-coding: utf-8-*-
# @Time  :2023/2/24 22:46
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2485_FindThePivotInteger.py

'''
[2485. Find the Pivot Integer]
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.

Constraints:

1 <= n <= 1000
'''

from math import sqrt


class Solution:

    def recursion_pivot(self, a, b):
        c, d = b - 1, b - 1
        for i in range(a, b):
            c -= i

            if c == 0 and i + 1 == d - 1:
                return i + 1

            if c > 0:
                continue
            elif c < 0:
                c += d - 1
                d -= 1
            else:
                return self.recursion_pivot(i + 1, d)
        return -1

    def pivotIntegerV1(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = n, n
        for i in range(1, n + 1):
            a -= i
            if a >= 0:
                if a == 0 and i + 1 == b - 1:
                    return i + 1
                continue
            else:
                a += b - 1
                b -= 1
        return -1

    def pivotIntegerV2(self, n: int) -> int:
        if n == 1:
            return 1
        return self.recursion_pivot(1, n + 1)

    a, b, c = 1, 0, 0

    def pivotIntegerV3(self, n: int) -> int:
        if Solution.a == 1:
            Solution.b, Solution.c = n, n
        else:
            Solution.c = n + 1

        if n == 1:
            return 1

        for i in range(Solution.a, n + 1):
            if Solution.b == 0 and i == Solution.c - 1:
                Solution.a = 1
                return i

            Solution.b -= i

            if Solution.b > 0:
                continue
            elif Solution.b < 0:
                Solution.b += Solution.c - 1
                Solution.c -= 1
            else:
                Solution.a = i + 1
                return self.pivotIntegerV3(Solution.c - 1)
        Solution.a = 1
        return -1

    def pivotIntegerV4(self, n: int) -> int:
        result = sqrt((n * (n + 1)) // 2)
        return int(result) if result % 1 == 0.0 else -1

    def pivotIntegerV5(self, n: int) -> int:
        val = int(sqrt(n * (n + 1) // 2))
        if val * val == n * (n + 1) // 2:
            return val
        return -1
