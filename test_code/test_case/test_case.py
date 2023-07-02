from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.July import LeetCode1255_MaximumScoreWordsFormedByLetters as l


class TestCase:

    def test_leetcode(self):
        expect1 = 23
        expect2 = 27
        expect3 = 0
        expect4 = 51
        expect5 = 49
        expect = [expect1, expect2, expect3, expect4, expect5]
        # expect = [expect5]

        t = td.GenTestData(self)
        r = []
        for i in t:
            r.append(l.Solution().maxScoreWords(i[0], i[1], i[2]))

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
