# -*-coding: utf-8-*-
# @Time  :2023/7/6 18:32
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1071_GreatestCommonDivisorOfStrings.py


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:


        sstr, lstr = "", ""
        if len(str1) > len(str2):
            lstr, sstr = str1, str2
        else:
            lstr, sstr = str2, str1

        if sstr * (len(lstr) // len(sstr)) == lstr:
            return sstr

        ml = len(sstr)

        for j in lstr[ml:]:
            if j not in sstr:
                return ""

        for i in range(ml - 1, -1, -1):
            if sstr[i] != lstr[i]:
                return ""
            else:
                tmp = sstr[:i+1]

                t, s, l = len(tmp), len(sstr), len(lstr)
                if s % t != 0 or l % t != 0:
                    continue
                else:
                    a, b = s // t, l // t
                    while tmp * a != sstr or tmp * b != lstr:
                        a -= 1
                        b -= 1

                        if a <= 0 or b <= 0:
                            return ""
                return tmp

