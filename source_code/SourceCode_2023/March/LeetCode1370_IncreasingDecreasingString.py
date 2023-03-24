# -*-coding: utf-8-*-
# @Time  :2023/3/24 14:36
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1370_IncreasingDecreasingString.py

'''
[LeetCode1370. Increasing Decreasing String]

You are given a string s. Reorder the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.


Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
'''


import collections


class SolutionV1:
    def sortString(self, s: str) -> str:

        count, res, l = 0, "", len(s)
        ls = list(s)
        os = ''.join(sorted(list(set(ls))))
        ros = os[::-1]

        c = collections.Counter(s)

        while len(res) < l:
            for i in os:
                if c.get(i) != 0:
                    res += i
                    c[i] -= 1

            for j in ros:
                if c.get(j) != 0:
                    res += j
                    c[j] -= 1

        return res


class SolutionV2:
    def sortString(self, s: str) -> str:
        a = [0] * 26
        for i in s:
            a[ord(i) - 97] += 1

        res = ""

        while len(res) < len(s):
            for j in range(26):
                if a[j] != 0:
                    res += chr(j + 97)
                    a[j] -= 1

            for k in range(25, -1, -1):
                if a[k] != 0:
                    res += chr(k + 97)
                    a[k] -= 1

        return res
