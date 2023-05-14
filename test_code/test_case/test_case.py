import time

from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.May import LeetCode1030_MatrixCellsInDistanceOrder as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().allCellsDistOrder(i[0], i[1], i[2], i[3]))

        expect1 = [[0,0],[0,1]]
        expect2 = [[0,1],[0,0],[1,1],[1,0]]
        expect3 = [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
        # expect = [expect1, expect2,expect3]
        expect = [expect3]
        # print(r)

        for j in range(len(r)):
            print(r[j])
            # if r[j] != expect[j]:
            #     print(r[j])
        return r == expect

start = time.time()
res = TestCase()
res.test_leetcode()
print(time.time() - start)