# -*-coding: utf-8-*-
# @Time  :2023/6/30 5:58
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode1356_SortIntegersByTheNumberOf1Bits.py


'''
[1356. Sort Integers by The Number of 1 Bits]
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.



Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]
Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.


Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 104
'''

import collections
from typing import List


class SolutionV1:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        arr.sort()

        for i in arr:
            c = bin(i).count('1')
            if c not in d:
                d[c] = [i]
            else:
                d[c].append(i)

        res = []
        keys = list(d.keys())
        keys.sort()

        for j in keys:
            res.extend(d[j])

        return res


class SolutionV2:
    def sortByBits(self, arr: List[int]) -> List[int]:

        arr = sorted(arr,key = lambda num: (num[0],num[1]))
        return arr

