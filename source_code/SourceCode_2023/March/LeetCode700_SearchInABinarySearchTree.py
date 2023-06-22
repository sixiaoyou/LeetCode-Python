# -*-coding: utf-8-*-
# @Time  :2023/3/4 18:30
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode700_SearchInABinarySearchTree.py

'''
[LeetCode700. Search in a Binary Search Tree]
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]


Input: root = [4,2,7,1,3], val = 5
Output: []
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    test = None

    def subSearchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return

        if root.val == val:
            Solution.test = root
            return Solution.test

        self.subSearchBST(root.left, val)
        self.subSearchBST(root.right, val)

        return Solution.test

    def searchBSTV1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        Solution.test = None
        return self.subSearchBST(root, val)

    def searchBSTV2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        res = None
        if val > root.val:
            root = root.right
            res = self.searchBST(root, val)
        elif val < root.val:
            root = root.left
            res = self.searchBST(root, val)
        else:
            res = root
            return res
        return res
