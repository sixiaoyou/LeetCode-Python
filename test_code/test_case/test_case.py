import time

from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.June import LeetCode1991_FindTheMiddleIndexInArray as l


class TestCase:

    def test_leetcode(self):
        expect1 = 3
        expect2 = 2
        expect3 = -1
        expect4 = 0
        expect5 = 1
        expect6 = 1

        expect = [expect1, expect2, expect3, expect4, expect5, expect6]
        expect = [expect6]

        t = td.GenTestData(self)
        r = []
        for i in range(len(t)):
            r.append(l.Solution().findMiddleIndex(t[i]))

        print(f'real: {r}, expect:{expect}')

        # for j in range(len(r)):
        #     if r[j] != expect[j]:
        #         print(f'Failed!!!\ndata: {t[j]}\nreal: {r[j]}\nexpect:{expect[j]}')
        #     pass

        return r == expect


# start = time.time()
res = TestCase()
print(res.test_leetcode())
# print(time.time() - start)
