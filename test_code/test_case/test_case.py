import time

from test_code.test_data.test_data import Test_Data as td
from source_code.SourceCode_2023.June import LeetCode2737_FindTheClosestMarkedNode as l


class TestCase:

    def test_leetcode(self):
        expect1 = 4
        expect2 = 3
        expect3 = -1
        expect4 = 2
        expect5 = 6
        expect6 = 2
        expect7 = 1368122
        expect8 = 3
        expect9 = 8
        expect10 = 12

        expect = [expect1, expect2, expect3, expect4, expect5, expect6, expect8,expect9]
        # expect = [expect2, expect3, expect5]
        # expect = [expect9]


        

        t = td.GenTestData(self)
        r = []
        for i in range(len(t)):
            print(f'length:{len(t[i][3])}')
            print(f'nodes: {t[i][0]}, Origin Graph:{t[i][1]}')
            print(f'start_node: {t[i][2]}, dest_node:{t[i][3]}\n')
            r.append(l.Solution().minimumDistance(t[i][0], t[i][1], t[i][2], t[i][3]))
            print(f'Expect: {expect[i]} ')
            print("**************************************************\n")
        
        
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