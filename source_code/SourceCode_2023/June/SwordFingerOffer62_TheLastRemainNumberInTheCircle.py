# -*-coding: utf-8-*-
# @Time  :2023/6/9 19:13
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: SwordFingerOffer62_TheLastRemainNumberInTheCircle.py.py

'''
[��ָ Offer 62. ԲȦ�����ʣ�µ�����]
0,1,������,n-1��n�������ų�һ��ԲȦ��������0��ʼ��ÿ�δ����ԲȦ��ɾ����m�����֣�ɾ�������һ�����ֿ�ʼ��������������ԲȦ��ʣ�µ����һ�����֡�

���磬0��1��2��3��4��5���������һ��ԲȦ��������0��ʼÿ��ɾ����3�����֣���ɾ����ǰ4������������2��0��4��1��������ʣ�µ�������3��



ʾ�� 1��

����: n = 5, m = 3
���: 3
ʾ�� 2��

����: n = 10, m = 17
���: 2


���ƣ�

1 <= n <= 10^5
1 <= m <= 10^6
'''

class Solution:

    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i

        return f
