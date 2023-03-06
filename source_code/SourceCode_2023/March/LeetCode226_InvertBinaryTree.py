# -*-coding: utf-8-*-
# @Time  :2023/3/6 14:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode226_InvertBinaryTree.py


'''
[LeetCode226. Invert Binary Tree]
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
from collections import deque


class Solution:
    def invertTreeV1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        dq = deque()
        dq.append(root)
        iroot = copy.deepcopy(dq[0])
        flag = True

        while dq:
            if flag:
                iroot = dq[0]
                flag = False

            root = dq.pop()
            root.left, root.right = root.right, root.left

            if root.left:
                dq.append(root.left)

            if root.right:
                dq.append(root.right)

        return iroot



    def invertTreeV2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        self.invertTreeV2(root.left)
        self.invertTreeV2(root.right)
        root.left, root.right = root.right, root.left

        return root