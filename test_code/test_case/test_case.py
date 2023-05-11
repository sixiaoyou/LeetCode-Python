from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.May import LeetCode2418_SortThePeople as l


class TestCase:

    def test_leetcode(self):
        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().sortPeople(i))

        expect1 = ["Mary","Emma","John"]
        expect2 = ["Bob","Alice","Bob"]
        expect = [expect1, expect2]
        print(r)

        for j in range(len(r)):
            if r[j] != expect[j]:
                print(r[j])
        return r == expect

res = TestCase()
print(res.test_leetcode())