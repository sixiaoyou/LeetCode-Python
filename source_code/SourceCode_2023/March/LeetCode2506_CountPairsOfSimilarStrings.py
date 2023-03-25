# -*-coding: utf-8-*-
# @Time  :2023/3/25 11:58
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2506_CountPairsOfSimilarStrings.py


'''
[LeetCode2506. Count Pairs Of Similar Strings]
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.



Example 1:

Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'.
Example 2:

Input: words = ["aabb","ab","ba"]
Output: 3
Explanation: There are 3 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'.
- i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
- i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.
Example 3:

Input: words = ["nba","cba","dba"]
Output: 0
Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consist of only lowercase English letters.
'''


import collections
from typing import List


class SolutionV1:
    def similarPairs(self, words: List[str]) -> int:
        sw = list(map(lambda x: ''.join(sorted(list(set(list(x))))), words))
        res = 0

        c = collections.Counter(sw)
        for i in c:
            res += c[i] * (c[i] - 1) // 2

        return res


from collections import Counter


class SolutionV2:
    def similarPairs(self, words: List[str]) -> int:
        res, c = 0, Counter()

        for i in words:
            count = 0
            for k in i:
                count |= 1 << (ord(k) - 97)
            c[count] += 1

        for j in c.values():
            res += j * (j - 1) // 2

        return res
