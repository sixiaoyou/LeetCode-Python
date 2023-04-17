# -*-coding: utf-8-*-
# @Time  :2023/4/17 7:45
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode942_DIStringMatch.py


'''
[LeetCode942. DI String Match]
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.



Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]


Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.
'''


class SolutionV1:
    def diStringMatch(self, s: str) -> List[int]:

        res = []
        sl = len(s)
        count, recount = 0, 0

        for i in range(sl):
            if s[i] == 'I':
                res.append(count)
                count += 1
            else:
                res.append(sl - recount)
                recount += 1

        lnum = count if s[-1] == 'I' else sl - recount
        res.append(lnum)
        return res





