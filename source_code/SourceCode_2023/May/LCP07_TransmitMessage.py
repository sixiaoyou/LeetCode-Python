# -*-coding: utf-8-*-
# @Time  :2023/5/29 13:58
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LCP07_TransmitMessage.py
import collections
from typing import List

class Solution:
            def numWays(self, n: int, relation: List[int], k: int) -> int:
                self.ways, self.n, self.k = 0, n, k
                self.edges = collections.defaultdict(list)
                for src, dst in relation:
                    self.edges[src].append(dst)
                print(self.edges)

                self.dfs(0, 0)
                return self.ways

            def dfs(self, index, steps):
                if steps == self.k:
                    if index == self.n - 1:
                        self.ways += 1
                    return
                for to in self.edges[index]:
                    print(to, steps)
                    self.dfs(to, steps + 1)

