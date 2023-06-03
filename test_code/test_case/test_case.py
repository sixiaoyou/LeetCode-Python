import time

from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.May import LCP07_TransmitMessage as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().numWays(i[0], i[1], i[2]))

        expect1 = 3
        expect2 = 0
        expect3 = 1
        expect4 = 11
        expect5 = 3

        expect = [expect1, expect2, expect3, expect4, expect5]
        print(r)

        for j in range(len(r)):
            # if r[j] != expect[j]:
            #     print(r[j])
            pass

        return r == expect


res = TestCase()
res.test_leetcode()
