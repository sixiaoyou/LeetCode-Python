# -*-coding: utf-8-*-
# @Time  :2023/6/6 9:56
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: SwordFingerOffer6-PrintLinkedListFromEndToEnd.py

'''
����һ�������ͷ�ڵ㣬��β��ͷ����������ÿ���ڵ��ֵ�������鷵�أ���

ʾ�� 1��

���룺head = [1,3,2]
�����[2,3,1]


���ƣ�

0 <= ������ <= 10000
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []

        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

