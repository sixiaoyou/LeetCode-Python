# -*-coding: utf-8-*-
# @Time  :2023/6/7 9:15
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: SwordFingerOffer24_ReverseLinkedList.py

'''
[206. 反转链表]
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionV1:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        c = 0

        rhead = head
        while head.next is not None:
            head = head.next
            c += 1

        head1 = lhead = head

        while c != 1:
            head = rhead
            while head.next is not None:
                head = head.next
                if head.next is not None and head.next.next is None:
                    head.next = None
            lhead.next = head
            lhead = lhead.next
            c -= 1

        rhead.next = None
        lhead.next = rhead
        return head1


class SolutionV2:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None

        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp

        return pre

