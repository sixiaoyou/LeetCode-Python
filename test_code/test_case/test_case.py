import time

from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.May import LeetCode1380_LuckyNumbersInAMatrix as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().luckyNumbers(i))

        expect1 = [15]
        expect2 = [12]
        expect3 = [7]
        expect4 = []
        expect5 = [18811]
        expect = [expect1, expect2,expect3, expect4, expect5]
        expect = [expect3]
        print(r)

        for j in range(len(r)):
            pass
            # print(r[j])
            # if r[j] != expect[j]:
            #     print(r[j])
        return r == expect

start = time.time()
res = TestCase()
res.test_leetcode()
# print(time.time() - start)