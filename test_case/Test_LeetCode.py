# -*-coding: utf-8-*-
# @Time  :2023/2/19 18:52
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: Test_LeetCode.py

'''
Note:
Test source_code/SourceCode_2023/February/LeetCode2500_DeleteGreatestValueInEachRow
'''

from source_code.SourceCode_2023.February.LeetCode2500_DeleteGreatestValueInEachRow import Solution


class Test_LeetCode(Solution):

    def setup(self):
        print("Initialize test...")

    def teardown(self):
        print("Clear test...")

    def test_solution(self):
        grid = [[1,2,4],[3,3,1]]
        assert self.deleteGreatestValueV1(grid) == 8
        assert self.deleteGreatestValueV2(grid) == 8
        assert self.deleteGreatestValueV3(grid) == 8
        assert self.deleteGreatestValueV4(grid) == 8
