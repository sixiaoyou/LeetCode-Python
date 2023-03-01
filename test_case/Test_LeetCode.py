# -*-coding: utf-8-*-
# @Time  :2023/2/19 18:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: Test_LeetCode.py

'''
Note:
Test source_code/SourceCode_2023/February/LeetCode2331_EvaluateBooleanBinaryTree
'''
from source_code.SourceCode_2023.February.LeetCode2331_EvaluateBooleanBinaryTree import Solution
from source_code.common.convert_list_to_binaryTree import CreateBiTree


class Test_LeetCode(Solution):

    def setup(self):
        print("Initialize test...")

    def teardown(self):
        print("Clear test...")

    def test_solution(self):
        test_data = "213##01"
        c = CreateBiTree(test_data)
        root = c()
        so = Solution()

        assert so.SolutionV1().evaluateTree(root) is True
        assert so.SolutionV2().evaluateTree(root) is True
        assert so.SolutionV3().evaluateTree(root) is True
        assert so.SolutionV4().evaluateTree(root) is True
