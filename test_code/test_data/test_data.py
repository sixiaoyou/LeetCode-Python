# -*-coding: utf-8-*-
# @Time  :2023/4/29 15:23
# @Author: sixiaoyou
# @Email: 834628301@qq.com
# @File: test_data.py
import collections


class Test_Data:

    def GenTestData(self):
        words1 = ["dog", "cat", "dad", "good"]
        letters1 = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
        score1 = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        words2 = ["xxxz", "ax", "bx", "cx"]
        letters2 = ["z", "a", "b", "c", "x", "x", "x"]
        score2 = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]

        words3 = ["leetcode"]
        letters3 = ["l", "e", "t", "c", "o", "d"]
        score3 = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

        words4 = ["add", "dda", "bb", "ba", "add"]
        letters4 = ["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c", "c", "d", "d", "d"]
        score4 = [3, 9, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        words5 = ["da", "ac", "aba", "abcc", "cadc"]
        letters5 = ["a", "a", "a", "a", "b", "c", "c", "c", "d", "d", "d"]
        score5 = [3, 7, 9, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        t1 = [words1, letters1, score1]
        t2 = [words2, letters2, score2]
        t3 = [words3, letters3, score3]
        t4 = [words4, letters4, score4]
        t5 = [words5, letters5, score5]
        t = [t1, t2, t3, t4, t5]
        # t = [t5]

        return t


