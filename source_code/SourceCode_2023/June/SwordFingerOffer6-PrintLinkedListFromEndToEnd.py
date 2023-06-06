# -*-coding: utf-8-*-
# @Time  :2023/6/6 9:56
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: SwordFingerOffer6-PrintLinkedListFromEndToEnd.py

'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]


限制：

0 <= 链表长度 <= 10000
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

