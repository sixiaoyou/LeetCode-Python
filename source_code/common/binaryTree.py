# -*-coding: utf-8-*-
# @Time  :2023/2/28 22:38
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: convert_list_to_binaryTree.py
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CreateBiTree:

    def __init__(self, str_tree):
        self.str_tree = str_tree

    def create_tree(self):
        l1 = list(self.str_tree)
        l1 = [None if i == '#' else i for i in l1]

        nodes = [TreeNode(int(l1[i])) if l1[i] else None for i in range(len(l1))]

        root = nodes[0]
        for i in range(len(l1)):
            if 2 * i + 2 > len(l1):
                break
            cur_code = nodes[i]
            if nodes[2 * i + 1] is not None:
                cur_code.left = nodes[2 * i + 1]
            if nodes[2 * i + 2] is not None:
                cur_code.right = nodes[2 * i + 2]

        return root

    def __call__(self):
        return self.create_tree()

class Traversal:
    def __init__(self):
        self.res = []

    def pre_order(self, root):
        if root is None:
            return None

        self.res.append(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

        return self.res

    def in_order(self, root):
        if root is None:
            return None

        self.in_order(root.left)
        self.res.append(root.val)
        self.in_order(root.right)

        return self.res

    def post_order(self, root):
        if root is None:
            return None

        self.post_order(root.left)
        self.post_order(root.right)
        self.res.append(root.val)

        return self.res


    def level_order(self, root):
        if root is None:
            return None
        self.res = []
        dq = deque()
        res = []
        dq.append(root)
        while dq:
            root = dq.popleft()
            res.append(root.val)
            if root.left:
                dq.append(root.left)

            if root.right:
                dq.append(root.right)

        return res
