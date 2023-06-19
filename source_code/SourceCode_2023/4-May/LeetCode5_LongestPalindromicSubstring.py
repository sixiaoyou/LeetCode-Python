# -*-coding: utf-8-*-
# @Time  :2023/4/29 16:56
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode5_LongestPalindromicSubstring.py

'''
[LeetCode5. Longest Palindromic Substring]
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def string_traversal(self, start, end, l, s):
        while start > -1 and end < l and s[start] == s[end]:
            start -= 1
            end += 1

        return start, end

    def longestPalindrome(self, s: str) -> str:
        l = len(s)

        start, end = 0, l - 1
        end, start = self.string_traversal(end, start, l, s)

        if start >= end:
            return s

        sl, res = 0, ""
        for i in range(1, l):
            start, now = i - 1, i
            end = i if i == l - 1 else i + 1

            if s[start] == s[now]:
                if s[start] != s[end]:
                    start, now = self.string_traversal(start, now, l, s)
                    while start > -1 and now < l and s[start] == s[now]:
                        start -= 1
                else:
                    now = end if end < l - 1 and s[start] != s[end + 1] else now
                    if end < l - 1 and s[start] != s[end + 1]:
                        start, now = self.string_traversal(start, now, l, s)
                    else:
                        start, now = self.string_traversal(start, now, l, s)
                        if start > -1 and now < l and s[start + 1] == s[now]:
                            while now < l and s[start + 1] == s[now]:
                                now += 1
                sl = now - start - 1
            elif end < l and s[start] == s[end]:
                start, end = self.string_traversal(start, end, l, s)
                sl = end - start - 1
            end = end if end > now else now
            res = s[start + 1: end] if sl > len(res) else res
        return res if res else s[0]
