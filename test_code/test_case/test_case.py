import time

from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.May import LeetCode704_BinarySearch as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().search(i[0], i[1]))

        expect1 = 4
        expect2 = -1
        expect3 = 0
        expect4 = 1
        expect = [expect1, expect2, expect3, expect4]
        print(r)

        for j in range(len(r)):
            if r[j] != expect[j]:
                print(r[j])
        return r == expect


res = TestCase()
res.test_leetcode()