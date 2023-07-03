# encoding: utf-8
# @Time  :2023/6/1 15:04
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: X.py
import collections
import math
from collections import Counter
import time
from collections import Counter


class X:
    def test_explore(self):
        n1, n2 = 784, 98

        print(n1 / n2)
        print(n1 - n2)
        print(n1 + n2)
        print(n1 * n2)
        nums = [8, 686, 882, 76832]

        for n in nums:
            def get_next(n):
                total_sum = 0
                while n > 0:
                    n, digit = divmod(n, 10)
                    total_sum += digit ** 2
                return total_sum

            seen = set()
            while n != 1 and n not in seen:
                seen.add(n)
                n = get_next(n)

            print(n == 1)



a = X()
print(a.test_explore())

