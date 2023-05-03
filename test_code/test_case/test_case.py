from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.May import LeetCode_PalindromePermutationLCCI as l


class TestCase:

    def test_leetcode(self):
        tdl= td().GenTestData()
        expect_result = [True, False, True, False]
        # expect_result = [True]
        # expect_result = [False]

        t = l.Solution()
        res = []

        for i in range(len(tdl)):
            tmp = t.canPermutePalindrome(tdl[i])
            if tmp != expect_result[i]:
                print(f"source_data: {tdl[i]}, real_result: {tmp}, expect_result: {expect_result[i]}")
            res.append(tmp)

        return res == expect_result


res = TestCase()
print(res.test_leetcode())