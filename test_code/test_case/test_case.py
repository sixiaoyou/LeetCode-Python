from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.May import LeetCode1122_RelativeSortArray as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().relativeSortArray(i[0], i[1]))

        expect1 = [2,2,2,1,4,3,3,9,6,7,19]
        expect2 = [22,28,8,6,17,44]

        expect = [expect1, expect2]

        for j in range(len(r)):
            if r[j] != expect[j]:
                print(r[j])
        return r == expect

res = TestCase()
print(res.test_leetcode())