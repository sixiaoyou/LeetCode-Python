# -*-coding: utf-8-*-
# @Time  :2023/6/7 9:15
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: SwordFingerOffer24_ReverseLinkedList.py

'''
[206. ��ת����]
���㵥�����ͷ�ڵ� head �����㷴ת���������ط�ת�������

ʾ�� 1��
���룺head = [1,2,3,4,5]
�����[5,4,3,2,1]

ʾ�� 2��
���룺head = [1,2]
�����[2,1]

ʾ�� 3��
���룺head = []
�����[]
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

