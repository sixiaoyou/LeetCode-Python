# -*-coding: utf-8-*-
# @Time  :2023/7/2 10:12
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode884_UncommonWordsFromTwoSentences.py


'''
[884. Uncommon Words from Two Sentences]
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.



Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]


Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
'''

from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cs = Counter((s1 + " " + s2).split(" "))
        return list(filter(lambda x: cs[x] == 1, cs))

