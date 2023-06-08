import time

from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.June import LeetCode1880_CheckIfWordEqualsSummationOfTwoWords as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().isSumEqual(i[0], i[1], i[2]))

        expect1 = True
        expect2 = False
        expect3 = True
        expect4 = 11
        expect5 = 3

        expect = [expect1, expect2, expect3, expect4, expect5]
        expect = [expect1, expect2, expect3]
        print(r)

        for j in range(len(r)):
            if r[j] != expect[j]:
                print(f'Failed!!!\ndata: {t[j]}\nreal: {r[j]}\nexpect:{expect[j]}')
            pass

        return r == expect


res = TestCase()
res.test_leetcode()
