# -*-coding: utf-8-*-
# @Time  :2023/2/20 7:53
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2520_CountTheDigitsThatDivideANumber.py

'''
[LeetCode2520. Count the Digits That Divide a Number]

Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.



Example 1:

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.
Example 2:

Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
Example 3:

Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.


Constraints:

1 <= num <= 109
num does not contain 0 as one of its digits.

'''

import math


class Solution:
    def countDigitsV1(self, num: int) -> int:
        return len(list(filter(lambda x: num % int(x) == 0, list(str(num)))))


    def countDigits(self, num: int) -> int:
        count = 0
        cnum = num
        while num != 0:
            if cnum % (num % 10) == 0:
                count += 1
            num = math.floor(num / 10)
        return count

