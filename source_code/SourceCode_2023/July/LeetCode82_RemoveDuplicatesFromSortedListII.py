# -*-coding: utf-8-*-
# @Time  :2023/7/8 7:13
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode82_RemoveDuplicatesFromSortedListII.py

'''
¡¾To be optimum¡¿
[82. Remove Duplicates from Sorted List II]
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        s = ListNode(0)
        res = s
        pre = head
        head = head.next
        f = 0

        a, b = copy.deepcopy(pre), copy.deepcopy(head)
        a.next = None

        while head:
            if head.next and pre.val != head.val and head.val != head.next.val:
                tmp = copy.deepcopy(head)
                tmp.next = None
                s.next = tmp
                s = s.next

            pre = head
            head = head.next

            if head and head.next == None and pre.val != head.val:
                s.next = head

        if a.val != b.val:
            f = 1
            a.next = res.next

            if b.next == None:
                a.next = b
                return a

        return a if f else res.next
