# -*-coding: utf-8-*-
# @Time  :2023/2/28 19:33
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: LeetCode2331_EvaluateBooleanBinaryTree.py

'''
[LeetCode2331. Evaluate Boolean Binary Tree]
You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.
'''

from typing import Optional
from source_code.common.convert_list_to_binaryTree import TreeNode, CreateBiTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

tmp = []


class Solution:
    # 先序遍历（回溯)
    class SolutionV1():

        def evaluateTree(self, root: Optional[TreeNode]) -> bool:

            stack, tmp = [], []
            d = {0: False, 1: True, 2: "or", 3: "and"}
            rd = {False: 0, True: 1}

            while root is not None or len(stack) > 0:
                while root is not None:
                    tmp.append(root.val)
                    stack.append(root)
                    root = root.left

                if len(stack) > 0:
                    root = stack.pop()
                    root = root.right

            while len(tmp) > 3:
                i, a = 0, []
                while i < len(tmp):
                    if i < len(tmp) - 2:
                        if tmp[i] in [2, 3] and tmp[i + 1] in [0, 1] and tmp[i + 2] in [0, 1]:
                            tmp[i], tmp[i + 1], tmp[i + 2] = rd[eval(
                                f'{d[tmp[i + 1]]} {d[tmp[i]]} {d[tmp[i + 2]]}')], '', ''
                            i += 3
                        else:
                            i += 1
                    else:
                        i += 1

                a = [j for j in tmp if j != '']
                tmp = a

            b = "".join([str(k) for k in tmp])
            if b == "1" or (b.count('1') == 2 or ('1' in b and '2' in b)):
                return True
            else:
                return False

    #先序遍历（回溯 + 递归）
    class SolutionV2:

        def evaluateTree(self, root: Optional[TreeNode]) -> bool:

            stack, tmp = [], []
            while root is not None or len(stack) > 0:
                while root is not None:
                    tmp.append(root.val)
                    stack.append(root)
                    root = root.left

                if len(stack) > 0:
                    root = stack.pop()
                    root = root.right

            return self.get_res(tmp)

        def get_res(self, tmp):

            if len(tmp) <= 3:
                b = "".join([str(k) for k in tmp])
                if b == "1" or (b.count('1') == 2 or ('1' in b and '2' in b)):
                    return True
                else:
                    return False

            d = {0: False, 1: True, 2: "or", 3: "and"}
            rd = {False: 0, True: 1}
            i, a = 0, []

            while i < len(tmp):
                if i < len(tmp) - 2:
                    if tmp[i] in [2, 3] and tmp[i + 1] in [0, 1] and tmp[i + 2] in [0, 1]:
                        tmp[i], tmp[i + 1], tmp[i + 2] = rd[eval(
                            f'{d[tmp[i + 1]]} {d[tmp[i]]} {d[tmp[i + 2]]}')], '', ''
                        i += 3
                    else:
                        i += 1
                else:
                    i += 1

            a = [j for j in tmp if j != '']
            tmp = a

            return self.get_res(tmp)

    #先序遍历（非原方法递归）
    class SolutionV3:


        def evaluateTree(self, root: Optional[TreeNode]) -> bool:
            d = {0: False, 1: True, 2: "or", 3: "and"}
            rd = {False: 0, True: 1}

            self.pre_order_traversal(root)
            return self.get_res(rd, d)

        def pre_order_traversal(self, root: Optional[TreeNode]) -> bool:
            global tmp

            if root is None:
                return True

            tmp.append(root.val)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

        def get_res(self, rd, d):
            global tmp
            a = []
            while len(tmp) > 3:
                i = 0
                while i < len(tmp):
                    if i < len(tmp) - 2:
                        if tmp[i] in [2, 3] and tmp[i + 1] in [0, 1] and tmp[i + 2] in [0, 1]:
                            tmp[i], tmp[i + 1], tmp[i + 2] = rd[eval(
                                f'{d[tmp[i + 1]]} {d[tmp[i]]} {d[tmp[i + 2]]}')], '', ''
                            i += 3
                        else:
                            i += 1
                    else:
                        i += 1

                a = [j for j in tmp if j != '']
                tmp = a

            b = "".join([str(k) for k in tmp if k])
            if b == "1" or (b.count('1') == 2 or ('1' in b and '2' in b)):
                return True
            else:
                return False

    #先序遍历（原方法递归）
    class SolutionV4:

        def evaluateTree(self, root: Optional[TreeNode]) -> bool:
            if root.left is None:
                return root.val == 1

            if root.val == 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
