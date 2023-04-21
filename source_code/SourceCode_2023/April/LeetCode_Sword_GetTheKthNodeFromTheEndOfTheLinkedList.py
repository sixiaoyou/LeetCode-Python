# -*-coding: utf-8-*-
# @Time  :2023/4/21 17:18
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode_Sword_GetTheKthNodeFromTheEndOfTheLinkedList.py

'''
[��ָ Offer 22. �����е�����k���ڵ�]
����һ����������������е�����k���ڵ㡣Ϊ�˷��ϴ�����˵�ϰ�ߣ������1��ʼ�������������β�ڵ��ǵ�����1���ڵ㡣

���磬һ�������� 6 ���ڵ㣬��ͷ�ڵ㿪ʼ�����ǵ�ֵ������ 1��2��3��4��5��6���������ĵ����� 3 ���ڵ���ֵΪ 4 �Ľڵ㡣



ʾ����

����һ������: 1->2->3->4->5, �� k = 2.

�������� 4->5.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast=head
        slow=head
        for i in range(k):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        return slow