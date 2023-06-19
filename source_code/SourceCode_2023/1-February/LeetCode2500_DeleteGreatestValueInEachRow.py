# -*-coding: utf-8-*-
# @Time  :2023/2/23 10:44
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2500_DeleteGreatestValueInEachRow.py

'''
[LeetCode2500. Delete Greatest Value in Each Row]

You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.

Example 1:
Input: grid = [[1,2,4],[3,3,1]]
Output: 8
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.

Example 2:
Input: grid = [[10]]
Output: 10
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 100
'''
from typing import List

import numpy as np


class Solution:

    def deleteGreatestValueV1(self, grid: List[List[int]]) -> int:
        res = 0
        grid = list(map(lambda x: sorted(x), grid))
        for i in range(len(grid[0])):
            rl = []
            for j in range(len(grid)):
                rl.append(grid[j][i])
            res += max(rl)
        return res

    def deleteGreatestValueV2(self, grid: List[List[int]]) -> int:
        return int(sum(map(lambda x: max(x), np.transpose(list(map(lambda x: sorted(x), grid))))))

    def deleteGreatestValueV3(self, grid: List[List[int]]) -> int:
        res = 0
        grid = list(map(lambda x: sorted(x), grid))
        for i in range(len(grid[0])):
            currmax = 0
            for j in range(len(grid)):
                currmax = max(currmax, grid[j][i])
            res += currmax
        return res

    def deleteGreatestValueV4(self, grid: List[List[int]]) -> int:
        res = 0
        for k in grid:
            k.sort()
        for i in range(len(grid[0])):
            currmax = 0
            for j in range(len(grid)):
                currmax = max(currmax, grid[j][i])
            res += currmax
        return res
