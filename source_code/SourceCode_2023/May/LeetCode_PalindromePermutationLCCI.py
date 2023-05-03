'''
[ÃæÊÔÌâ 01.04. Palindrome Permutation LCCI]
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.



Example1:

Input: "tactcoa"
Output: true£¨permutations: "tacocat"¡¢"atcocta", etc.£©
'''

import collections


class SolutionV1:
    def canPermutePalindrome(self, s: str) -> bool:
        l = len(s)

        if l == 1:
            return True

        ls = list(s)
        ls.sort()

        slow, fast = 0, 1
        count, sl = 0, 0

        while fast < l:

            while fast < l and ls[slow] == ls[fast]:
                fast += 1

            if fast > l - 1:
                break

            sl = fast - slow
            slow = fast
            fast += 1

            count += 1 if sl % 2 == 1 else count
            if count > 1:
                return False

        count = count + 1 if ls[-1] != ls[-2] or (sl % 2 == 1 and sl != 1) else count
        return count < 2

class SolutionV2:
    def canPermutePalindrome(self, s: str) -> bool:
        c = collections.Counter(s)
        count = 0

        for i in c:
            if c[i] % 2 != 0:
                count += 1
            if count > 1:
                return False
        return True
