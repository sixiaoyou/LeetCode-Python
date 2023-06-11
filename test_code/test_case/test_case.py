import time

from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.June import SwordFingerOffer62_TheLastRemainNumberInTheCircle as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().lastRemaining(i[0], i[1]))

        expect1 = 3
        expect2 = 2
        expect3 = 9966

        expect = [expect1, expect2]
        expect = [expect3]
        print(r)

        # for j in range(len(r)):
        #     if r[j] != expect[j]:
        #         print(f'Failed!!!\ndata: {t[j]}\nreal: {r[j]}\nexpect:{expect[j]}')
        #     pass
        #
        # return r == expect



start = time.time()
res = TestCase()
res.test_leetcode()
print(time.time() - start)