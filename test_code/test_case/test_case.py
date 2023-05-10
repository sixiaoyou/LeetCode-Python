from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.May import LeetCode2437_NumberOfValidClockTimes as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().countTime(i))

        expect = [2, 100, 1440, 240, 240, 6, 2]
        # expect = [2, 100]
        print(r)

        for j in range(len(r)):
            if r[j] != expect[j]:
                print(r[j])
        return r == expect

res = TestCase()
print(res.test_leetcode())