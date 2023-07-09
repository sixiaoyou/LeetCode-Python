# -*-coding: utf-8-*-
# @Time  :2023/7/9 15:25
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode19_RemoveNthNodeFromEndOfList.py


'''
[19. Remove Nth Node From End of List]
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
'''


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        slow, fast = head, head

        while fast:
            fast = fast.next
            count += 1

            if count < n:
                if not fast:
                    return head.next

            elif count == n:
                if not fast:
                    return head.next
                else:
                    while fast and fast.next:
                        fast = fast.next
                        slow = slow.next

                        if not fast.next:
                            slow.next = slow.next.next
                            return head

                    head.next = head.next.next
                    return head

