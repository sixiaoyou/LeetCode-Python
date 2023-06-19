'''
[2737. Find the Closest Marked Node]
You are given a positive integer n which is the number of nodes of a 0-indexed directed weighted graph and a 0-indexed 2D array edges where edges[i] = [ui, vi, wi] indicates that there is an edge from node ui to node vi with weight wi.

You are also given a node s and a node array marked; your task is to find the minimum distance from s to any of the nodes in marked.

Return an integer denoting the minimum distance from s to any node in marked or -1 if there are no paths from s to any of the marked nodes.

Example 1:

Input: n = 4, edges = [[0,1,1],[1,2,3],[2,3,2],[0,3,4]], s = 0, marked = [2,3]
Output: 4
Explanation: There is one path from node 0 (the green node) to node 2 (a red node), which is 0->1->2, and has a distance of 1 + 3 = 4.
There are two paths from node 0 to node 3 (a red node), which are 0->1->2->3 and 0->3, the first one has a distance of 1 + 3 + 2 = 6 and the second one has a distance of 4.
The minimum of them is 4.


Example 2:

Input: n = 5, edges = [[0,1,2],[0,2,4],[1,3,1],[2,3,3],[3,4,2]], s = 1, marked = [0,4]
Output: 3
Explanation: There are no paths from node 1 (the green node) to node 0 (a red node).
There is one path from node 1 to node 4 (a red node), which is 1->3->4, and has a distance of 1 + 2 = 3.
So the answer is 3.


Example 3:

Input: n = 4, edges = [[0,1,1],[1,2,3],[2,3,2]], s = 3, marked = [0,1]
Output: -1
Explanation: There are no paths from node 3 (the green node) to any of the marked nodes (the red nodes), so the answer is -1.

Constraints:

2 <= n <= 500
1 <= edges.length <= 104
edges[i].length = 3
0 <= edges[i][0], edges[i][1] <= n - 1
1 <= edges[i][2] <= 106
1 <= marked.length <= n - 1
0 <= s, marked[i] <= n - 1
s != marked[i]
marked[i] != marked[j] for every i != j
The graph might have repeated edges.
The graph is generated such that it has no self-loops.
'''
import collections
from typing import List


class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        l = list(map(lambda x: x[0], edges))
        if s not in l:
            return -1

        d = collections.defaultdict(dict)
        for i in edges:
            if i[0] not in d:
                d[i[0]].update({i[1]: [i[1], i[2]]})
            else:
                if i[1] in d[i[0]]:
                    if d[i[0]][i[1]][1] > i[2]:
                        d[i[0]].update({i[1]: [i[1], i[2]]})
                else:
                    d[i[0]].update({i[1]: [i[1], i[2]]})

        return self.dijkstra(n, s, d, marked)

    def dijkstra(self, n, s, d, marked):

        res = float('inf')
        distances = [s] + [res] * n
        access = [0] * (n + 1)

        for x in d[s]:
            distances[x + 1] = min(distances[x + 1], d[s][x][1])

        for k in range(n):
            minDistanceFromStart = res
            minDistanceIndex = -1

            for index in range(n):
                if not access[index + 1] and distances[index + 1] < minDistanceFromStart:
                    minDistanceFromStart = distances[index + 1]
                    minDistanceIndex = index + 1

            if minDistanceIndex == -1:
                break

            access[minDistanceIndex] = 1
            for i in d[minDistanceIndex - 1].keys():
                if access[i + 1]:
                    continue
                weight = d[minDistanceIndex - 1][i][1]
                preDistance = distances[i + 1]

                if minDistanceFromStart + weight < preDistance:
                    distances[i + 1] = minDistanceFromStart + weight

        for i in marked:
            res = min(distances[i + 1], res)

        res = -1 if res == float('inf') else res
        return res
