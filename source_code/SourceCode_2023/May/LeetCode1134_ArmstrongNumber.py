# -*-coding: utf-8-*-
# @Time  :2023/5/21 6:58
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1134_ArmstrongNumber.py

'''
[1134. Armstrong Number]
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.



Example 1:

Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
Example 2:

Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.


Constraints:

1 <= n <= 108
'''

class Solution:
    def isArmstrong(self, n: int) -> bool:
        sn = str(n)
        l = len(sn)

        return sum(map(lambda x: int(x) ** l, sn)) == n