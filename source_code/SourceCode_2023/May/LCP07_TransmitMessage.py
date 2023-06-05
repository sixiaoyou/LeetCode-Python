# -*-coding: utf-8-*-
# @Time  :2023/5/29 13:58
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LCP07_TransmitMessage.py


'''
[LCP 07. ������Ϣ]
С���� A �ں� ta ��С������洫��Ϣ��Ϸ����Ϸ�������£�

�� n ����ң�������ұ�ŷֱ�Ϊ 0 �� n-1������С���� A �ı��Ϊ 0
ÿ����Ҷ��й̶������ɸ��ɴ���Ϣ��������ң�Ҳ����û�У�������Ϣ�Ĺ�ϵ�ǵ���ģ����� A ������ B ����Ϣ���� B ������ A ����Ϣ����
ÿ����Ϣ������Ҫ���ݸ���һ���ˣ�����Ϣ���ظ�����ͬһ����
����������� n���Լ��� [��ұ��,��Ӧ�ɴ�����ұ��] ��ϵ��ɵĶ�ά���� relation��������Ϣ��С A (��� 0 ) ���� k �ִ��ݵ����Ϊ n-1 ��С��鴦�ķ������������ܵ������ 0��

ʾ�� 1��

���룺n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3

�����3

���ͣ���Ϣ��С A ��� 0 ����ʼ���� 3 �ִ��ݣ������� 4������ 3 �ַ������ֱ��� 0->2->0->4�� 0->2->1->4�� 0->2->3->4��

ʾ�� 2��

���룺n = 3, relation = [[0,2],[2,1]], k = 2

�����0

���ͣ���Ϣ���ܴ�С A ������ 2 �ִ��ݵ���� 2

���ƣ�

2 <= n <= 10
1 <= k <= 5
1 <= relation.length <= 90, �� relation[i].length == 2
0 <= relation[i][0],relation[i][1] < n �� relation[i][0] != relation[i][1]
'''


import collections
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        self.index, self.ways, self.n, self.k = 0, 0, n, k
        self.existence = collections.defaultdict(list)

        for i, j in relation:
            self.existence[i].append(j)

        self.dfs(0, 0)
        return self.ways

    def dfs(self, index, steps):
        if steps == self.k:
            if index == self.n - 1:
                self.ways += 1
            return

        for df in self.existence[index]:
            self.dfs(df, steps + 1)

