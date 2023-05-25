# -*-coding: utf-8-*-
# @Time  :2023/5/25 8:22
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1180_CountSubstringsWithOnlyOneDistinctLetter.py

'''
[1180. Count Substrings with Only One Distinct Letter]
Given a string s, return the number of substrings that have only one distinct letter.



Example 1:

Input: s = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: s = "aaaaaaaaaa"
Output: 55


Constraints:

1 <= s.length <= 1000
s[i] consists of only lowercase English letters.
'''


class Solution:
    def countLetters(self, s: str) -> int:
        i, l, count = 0, len(s), 0

        while i < l:
            j = i
            while i + 1 < l and s[i] == s[i + 1]:
                i += 1

            n = i - j + 1
            count += n + n * (n - 1) // 2
            i += 1

        return count
