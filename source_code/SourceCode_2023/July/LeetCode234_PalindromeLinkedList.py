# -*-coding: utf-8-*-
# @Time  :2023/7/7 14:17
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode234_PalindromeLinkedList.py


'''
¡¾To be optimum¡¿
[234. Palindrome Linked List]
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next

        return res == res[::-1]

