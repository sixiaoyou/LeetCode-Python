# -*-coding: utf-8-*-
# @Time  :2023/5/29 13:58
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LCP07_TransmitMessage.py


from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        if k == 1 and relation[0][0] == 0 and relation[0][1] == n - 1:
            return 1

        if k % 2 == 0:
            return 0


        s = list(filter(lambda x: x[0] == 0, relation))
        e = list(filter(lambda x: x[-1] == n - 1, relation))
        print(f's{s}\ne{e}')


        m = 0
        for i in s:
            if i in e:
                m += 1

        l = 0
        c, l, ls, le = 0, len(relation), len(s), len(e)
        ld = l - ls

        su = ls
        for z in range(len(s)):
            if s[z][0] == 0 and s[z][-1] == n - 1:
                su -= 1

        c = ls * le - su

        if k <= 3:
            return c

        ld = l - 1
        for j in range(1,k):
            c += ld * ld
        c -= m * ld + (l - m) * (ld - 1)

        return c

